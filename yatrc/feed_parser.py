import feedparser

from yatrc.model import Post


def load_feed(url: str):
    data = feedparser.parse(url)  # pylint: disable=no-member
    entries = data["entries"]
    feed = data["feed"]

    for entry in entries:
        post = Post(entry["title"], entry["link"], entry["summary"],
                    feed["title"])
        yield post
