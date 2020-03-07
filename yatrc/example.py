from collections import deque
from typing import Deque, List

from picotui.context import Context
from picotui.screen import Screen

import yatrc.feed_parser as fp
from yatrc.widgets import PostsWidget, VerboseWidget, WidgetContainer


class Controller:  # pylint: disable=too-few-public-methods
    def __init__(self, verbose_widget: VerboseWidget, list_widget: PostsWidget,
                 posts: List[fp.Post], actions: Deque):
        self.verbose_widget = verbose_widget
        self.list_widget = list_widget
        self.posts = posts
        self.actions = actions

    def handle_action(self):
        if self.actions:
            action = self.actions.pop()
            if action == 'verbose':
                index = self.list_widget.cur_line
                post = self.posts[index]
                self.verbose_widget.set_lines(post.verbose_view())
                self.verbose_widget.visible = True
                self.list_widget.visible = False
                return True
        return False


def main() -> None:
    posts = fp.load_feed(
        "https://www.opennet.ru/opennews/opennews_all_utf.rss")
    posts = list(posts)

    actions = deque()  # type: Deque

    with Context():
        Screen.cls()
        Screen.attr_reset()
        width, height = Screen.screen_size()
        list_widget = PostsWidget([post.list_view() for post in posts],
                                  actions)
        list_widget.visible = True

        verbose_widget = VerboseWidget(width, height, ["hello", "world"])

        controller = Controller(verbose_widget, list_widget, posts, actions)
        dialog = WidgetContainer(controller)

        dialog.add(0, 0, list_widget)
        dialog.add(0, 0, verbose_widget)
        dialog.loop()


if __name__ == "__main__":
    main()
