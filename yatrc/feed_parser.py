import feedparser
from typing import List


# pylint: disable=too-few-public-methods
class Post:
    def __init__(self, title, link, summary, feed):
        self.title = title
        self.link = link
        self.summary = summary
        self.feed = feed

    def list_view(self):
        return "[{}] {}".format(self.feed, self.title)

    def verbose_view(self) -> List[str]:
        return [self.list_view()]


def load_feed(url: str):
    data = feedparser.parse(url)  # pylint: disable=no-member
    entries = data["entries"]
    feed = data["feed"]

    for entry in entries:
        post = Post(entry["title"], entry["link"], entry["summary"],
                    feed["title"])
        yield post
