import feedparser

def foo():
    url = 'https://www.opennet.ru/opennews/opennews_all_utf.rss'
    d = feedparser.parse(url)
    feed = d['feed']
    print(feed['title'])
    # print(d)
    entries = d['entries']
    print(len(entries))

    entry = entries[0]
    print(dir(entry))
    print(entry.keys())
    print(entry['title'])
    print(entry['link'])

    print(entry['summary'])


class Post:
    def __init__(self, title, link, summary):
        self.title = title
        self.link = link
        self.summary = summary


def load_feed(url):
    data = feedparser.parse(url)
    entries = data['entries']
    for entry in entries:
        post = Post(entry['title'], entry['link'], entry['summary'])
        yield post



