# reddit_comment_scraper

This is a simple Python script that will scrape Reddit comments:

- Scrapes comments along with metadata from specified subreddits
- Saves results to `.json`
- Can extract just comments text from `.json` to `.txt`
- Uses Reddit's official API via `PRAW`

## Requirements

- Developed and tested with `Python 3.14.2`. Earlier versions may not be compatible.
- A Reddit API key is required.
  1. Create a Reddit developer application
  2. Select "script" as the application type
  3. Copy your `CLIENT ID` and `CLIENT SECRET`
  4. More info: https://www.reddit.com/r/reddit.com/wiki/api/

## Usage

1. Clone this project:

```
git clone https://github.com/dadams05/reddit_comment_scraper.git
```

2. Create a virtual environment:

```
py -m venv <name>
```

3. Install the `requirements.txt` file:

```
pip install -r requirements.txt
```

4. Create a `.env` file and put your API keys in:

```
CLIENT_ID="client_id_key"
CLIENT_SECRET="client_secret_key"
USER_AGENT="can_really_put_whatever_here"
```

5. Run `main.py` while in your virtual environment. It will scrape the subreddits specified in the script and save the results as a `.json` file in the specified output directory.

```
py main.py
```

6. There is one optional flag, `-e` or `--extract`. When using this flag, provide one of the scraped `.json` files and it will extract only the comments text out to a `.txt` file.

```
py main.py -e "scraped.json"
```

## Before Committing

1. Run `pip freeze > requirements.txt` if you install additional dependencies
2. Run `pylint <filename>` on any files you changed
3. Run `black <filename>` on any files you changed
