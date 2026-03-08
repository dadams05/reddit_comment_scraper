# reddit_comment_scraper

This is a simple Python script that will scrape Reddit comments:

- Scrapes comments along with metadata from specified subreddits
- Saves results to `.json`
- Can extract just comments text from `.json` to `.txt`
- Uses Reddit's official API via `PRAW`
- Filters out comments with blacklisted words

## Requirements

- Developed and tested with `Python 3.14.2`. Earlier versions may not be compatible.
- A Reddit API key is required:
  1. Create a Reddit developer application
  2. Select "script" as the application type
  3. Copy your `CLIENT ID` and `CLIENT SECRET`
  4. More info: https://www.reddit.com/r/reddit.com/wiki/api/

## Usage

1. Clone this project: `git clone https://github.com/dadams05/reddit_comment_scraper.git`

2. Create a virtual environment: `py -m venv <name>`

3. Activate the virtual environemnt:

   - Windows: `.\<name>\Scripts\activate`

   - Linux: `source <name>/bin/activate`

4. Install the `requirements.txt` file (make sure your venv is activated): `pip install -r requirements.txt`

5. Create a `.env` file and put your API keys in it. Check the example file called `.env.example`.

6. Run `main.py` while in your virtual environment. It will scrape the subreddits specified in the script and save the results as a `.json` file in the specified output directory: `py main.py`

There is one optional flag, `-e` or `--extract`. When using this flag, provide one of the scraped `.json` files and it will extract only the comments text out to a `.txt` file: `py main.py -e "scraped.json"`

## Before Committing

1. Run `pip freeze > requirements.txt` if any additional dependencies were installed.
2. Run `pylint <space separated filenames>` on any Python files changed.
3. Run `black <space separated filenames>` on any Python files changed.

## Example Run

This is example output of when the script is ran.

``` bash
(.venv) py .\main.py
>> Starting scraping
[Subreddit] wallstreetbets
[Post] ERII Energy Recovery Desalination
[Post] Who bought the most recent IPO? 🤡
[Post] I dont think this is talked about enough... (EU big pharma milking US cow DRY)
[Subreddit] smallstreetbets
[Post] This weeks plays(feat. Overnight SPYputs)
[Post] Stocks with strong fundamentals + major government contracts?
[Post] Ecopetrol (EC) – Political Control, Tax and Asymmetric Downside
[Subreddit] StockMarket
[Post] Yes, Snap Inc makes money. Yes, they have many users. Yes, the stock is undervalued.
[Post] BlackRock caps withdrawals amid credit fund strain
[Post] Will Iran war fallout end the bull market? When investors really need to worry
>> Filtering
>> Finished
>> Subreddits scraped: 3
>> Posts scraped:      9
>> Comments scraped:   263
>> Comments kept:      257
>> Time taken:         12.38 sec
```

This is a snippet from the `.json` file that is outputted.

``` json
[
    {
        "id": "o997l5k",
        "created": "2026-03-07 21:12:34",
        "score": 11,
        "text": "Sir, this is the casino. The mental hospital is two blocks down."
    },
    {
        "id": "o996vet",
        "created": "2026-03-07 21:12:34",
        "score": 10,
        "text": "Wut"
    },
    {
        "id": "o9970u4",
        "created": "2026-03-07 21:12:34",
        "score": 5,
        "text": "Ok"
    },
    {
        "id": "o999e7o",
        "created": "2026-03-07 21:12:34",
        "score": 5,
        "text": "I hope his mom brings him his hot pocket before he posts again."
    },
    {
        "id": "o9994km",
        "created": "2026-03-07 21:12:34",
        "score": 4,
        "text": "Reading rainbow over here"
    }
]
```
