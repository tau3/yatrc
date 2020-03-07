from typing import List


class Post:
    def __init__(self, title: str, link: str, summary: str, feed: str):
        self.title = title
        self.link = link
        self.summary = summary
        self.feed = feed

    def list_view(self):
        return "[{}] {}".format(self.feed, self.title)

    def verbose_view(self) -> List[str]:
        return [self.list_view()]
