from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import Dialog
from yatrc.widgets import PostsWidget, VerboseWidget
import yatrc.feed_parser as fp
from collections import deque
from typing import List, Deque


class Controller:
    def __init__(self, verbose_widget: VerboseWidget, list_widget: PostsWidget,
                 posts: List[fp.Post], actions: Deque):
        self.verbose_widget = verbose_widget
        self.list_widget = list_widget
        self.posts = list(posts)
        self.actions = actions

    def handle_action(self):
        if self.actions:
            action = self.actions.pop()
            if action == 'verbose':
                index = self.list_widget.cur_line
                try:
                    post = self.posts[index]
                except BaseException as ee:
                    print(index)
                    raise ee
                self.verbose_widget.set_lines(post.verbose_view())
                self.verbose_widget.visible = True
                self.list_widget.visible = False
                return True
        return False


class MyDialog(Dialog):
    def __init__(self, controller):
        width, height = Screen.screen_size()
        super().__init__(0, 0, width, height)
        self.controller = controller

    def loop(self):
        self.redraw()
        while True:
            if self.controller.handle_action():
                self.redraw()

            key = self.get_input()
            res = self.handle_input(key)

            if res is not None and res is not True:
                return res


def main() -> None:
    posts = fp.load_feed(
        "https://www.opennet.ru/opennews/opennews_all_utf.rss")
    posts = list(posts)

    actions = deque()

    with Context():
        Screen.cls()
        Screen.attr_reset()
        width, height = Screen.screen_size()
        list_widget = PostsWidget([post.list_view() for post in posts],
                                  actions)
        list_widget.visible = True

        verbose_widget = VerboseWidget(width, height, ["hello", "world"])

        controller = Controller(verbose_widget, list_widget, posts, actions)
        dialog = MyDialog(controller)

        dialog.add(0, 0, list_widget)
        dialog.add(0, 0, verbose_widget)
        dialog.loop()


if __name__ == "__main__":
    main()
