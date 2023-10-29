from gnews import GNews
from datetime import datetime
from newspaper import Config

config = Config()
config.fetch_images = False

'''Gets all articles regarding the keyword, limit the search with the date options, by default the last year. Retursn a dict with date as key, and an array of results as value.'''
def get_articles(keyword, start=None, end=None):
    print("Getting articles ...")
    # Initialize the google news package
    google_news = GNews(language='en')

    if start == None or end == None:
        google_news.period = '1m'
    else:
        google_news.start_date(start)
        google_news.end_date(end)

    print("Start querying GNews")
    news_result = google_news.get_news(keyword)

    dateNewsMap = dict()
    for article in news_result:
        date = article['published date']
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")

        if date not in dateNewsMap:
            dateNewsMap[date] = []

        try:
            # Get the full text
            article3k = google_news.get_full_article(article['url'])
            article3k.download(config)
            # full_text = article['description']
            dateNewsMap[date].append(article3k.text)
        except:
            # Ignore errors
            1+1

    return dateNewsMap