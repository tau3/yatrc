from collections import deque
from typing import Deque

from picotui.context import Context
from picotui.screen import Screen

import yatrc.feed_parser as fp
from yatrc.controller import Controller
from yatrc.view import PostsWidget, VerboseWidget


def main() -> None:
    posts = fp.load_feed(
        "https://www.opennet.ru/opennews/opennews_all_utf.rss")
    posts = list(posts)

    actions = deque()  # type: Deque

    with Context():
        Screen.cls()
        Screen.attr_reset()
        list_widget = PostsWidget([post.list_view() for post in posts],
                                  actions,
                                  is_visible=True)

        verbose_widget = VerboseWidget()

        controller = Controller(verbose_widget, list_widget, posts, actions)
        controller.loop()


if __name__ == "__main__":
    main()
