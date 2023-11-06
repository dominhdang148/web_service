import feedparser
NewsFeed = feedparser.parse(
    "https://genshin-feed.com/feed/rss-vi-updates.xml")
entries = NewsFeed.entries

for entry in entries:
    print(entry.title)
