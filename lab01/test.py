import feedparser
url = 'f'
NewsFeed = feedparser.parse(url)
entries = NewsFeed.entries

if entries:

    for entry in entries:
        print(entry.title)

else:
    print("entries is empty")
