from typing import List


class Post:
    def __init__(self, title: str, link: str, summary: str, feed: str):
        self.title = title
        self.link = link
        self.summary = summary
        self.feed = feed

    def list_view(self) -> str:
        return "[{}] {}".format(self.feed, self.title)

    def verbose_view(self, width: int) -> List[str]:
        summary = _chunks(self.summary, width)
        summary = list(summary)
        summary = summary[:5]
        return [self.list_view(), '', self.link, ''] + summary


def _chunks(seq, length):
    for i in range(0, len(seq), length):
        yield seq[i:i + length]
