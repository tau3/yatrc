import asyncio
from collections import deque
from typing import Deque

from picotui.context import Context
from picotui.screen import Screen

import yatrc.feed_parser as fp
from yatrc.controller import Controller
from yatrc.view import PostsWidget, VerboseWidget


async def main() -> None:
    posts = await fp.load_all_feeds()
    posts = list(posts)

    actions = deque()  # type: Deque

    with Context():
        Screen.cls()
        Screen.attr_reset()
        list_widget = PostsWidget([post.list_view() for post in posts],
                                  actions)

        verbose_widget = VerboseWidget(actions)

        controller = Controller(verbose_widget, list_widget, posts, actions)
        controller.loop()


if __name__ == "__main__":
    asyncio.run(main())
