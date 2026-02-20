# pylint: disable=missing-module-docstring
import os
import time
import json
import argparse
from datetime import datetime
from dotenv import load_dotenv
import praw

# API keys
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

# globals
OUT_DIRECTORY = "out"  # directory to output files
FILE_NAME = f"scrape_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json"  # name of file to save to
NUM_MAX_POSTS = 15  # max number of posts to scrape from for each subreddit
NUM_COMMENTS_REPLACE = 15  # depth of comment subtrees to replace; can be None
SUBREDDITS = [  # subreddits to scrape from
    "wallstreetbets",
    "smallstreetbets",
    "StockMarket",
    "Shortsqueeze",
    "investing",
    "Daytrading",
]
BLACKLIST = [  # comments containing these words/phrases will be filtered out
    "[deleted]",
    "[removed]",
    "I am a bot",
    "https://preview.redd.it/",
    "![gif](giphy",
    "**User Report**",
    "I will be messaging you in",
    "[**Join WSB Discord**]",
]


def scrape_comments():
    """Scrapes comments from Reddit"""
    # setup
    reddit = praw.Reddit(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT
    )
    comments = []
    subreddit_count = 0
    post_count = 0
    scraped_comment_count = 0
    filtered_comment_count = 0
    start_time = time.perf_counter()

    # scrape comments from several posts across several subreddits
    print(">> Starting scraping")
    for subreddit in SUBREDDITS:
        print(f"[Subreddit] {subreddit}")
        subreddit_count += 1
        for submission in reddit.subreddit(subreddit).new(limit=NUM_MAX_POSTS):
            print(f"[Post] {submission.title}")
            post_count += 1
            submission.comment_sort = "top"
            submission.comments.replace_more(limit=NUM_COMMENTS_REPLACE)
            time.sleep(1)  # to avoid rate limiting
            # store the comment data
            for comment in submission.comments.list():
                scraped_comment_count += 1
                comment_data = {}
                comment_data["id"] = comment.id
                comment_data["created"] = str(
                    datetime.fromtimestamp(submission.created_utc)
                )
                comment_data["score"] = comment.score
                comment_data["text"] = comment.body
                comments.append(comment_data)

    # filter out comments with blacklisted words (bot comments)
    print(">> Filtering")
    filtered = []
    for comment in comments:
        if any(keyword in comment["text"] for keyword in BLACKLIST):
            continue
        sanitized = comment["text"].replace("\n", " ")
        sanitized = " ".join(sanitized.split())
        comment["text"] = sanitized
        filtered.append(comment)
        filtered_comment_count += 1
    comments = filtered

    # save the comments to a file
    os.makedirs(OUT_DIRECTORY, exist_ok=True)
    with open(os.path.join(OUT_DIRECTORY, FILE_NAME), "w", encoding="utf-8") as file:
        json.dump(comments, file, indent=4, ensure_ascii=False)

    # wrap up and print metrics
    end_time = time.perf_counter()
    print(">> Finished")
    print(f">> Subreddits scraped: {subreddit_count}")
    print(f">> Posts scraped:      {post_count}")
    print(f">> Comments scraped:   {scraped_comment_count}")
    print(f">> Comments kept:      {filtered_comment_count}")
    print(f">> Time taken:         {(end_time - start_time):.2f} sec")


def extract_from_scrape(in_file_name: str, out_file_name="extracted.txt"):
    """Given a scraped .json file, will extract only the comments to a .txt file"""
    comments = []
    with open(in_file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        for comment in data:
            comments.append(comment["text"])

    with open(
        os.path.join(OUT_DIRECTORY, out_file_name), "w", encoding="utf-8"
    ) as file:
        for c in comments:
            file.write(c + "\n")


if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(
        prog="Reddit Comment Scraper",
        description="Program to scrape comments from subreddit posts",
    )
    parser.add_argument(
        "-e",
        "--extract",
        type=str,
        help="scraped .json file to extract comments text from",
    )
    args = parser.parse_args()

    if args.extract:
        extract_from_scrape(args.extract)
    else:
        scrape_comments()
