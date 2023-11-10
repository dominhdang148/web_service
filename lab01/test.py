import feedparser
from html import escape
url = 'https://vnexpress.net/rss/tin-moi-nhat.rss'
NewsFeed = feedparser.parse(url)
entries = NewsFeed.entries

if entries:

    for entry in entries[:2]:
        print(escape(entry.description))

else:
    print("entries is empty")
