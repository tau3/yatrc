import asyncio
import itertools
import os.path
from concurrent.futures import ProcessPoolExecutor

import feedparser

from yatrc.model import Post


def load_feed(url: str):
    data = feedparser.parse(url)  # pylint: disable=no-member
    entries = data["entries"]
    feed = data["feed"]

    return [
        Post(entry["title"], entry["link"], entry.get('summary', ''),
             feed['title']) for entry in entries
    ]


async def load_all_feeds():
    with open(os.path.expanduser('~/.newsboat/urls')) as source:
        urls = source.readlines()

    executor = ProcessPoolExecutor(len(urls))
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(executor, load_feed, url) for url in urls]
    done, _ = await asyncio.wait(tasks)

    return itertools.chain(*[d.result() for d in done])
