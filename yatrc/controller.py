from typing import Deque, List

from picotui.screen import Screen
from picotui.widgets import Dialog

import yatrc.feed_parser as fp
from yatrc.view import PostsWidget, VerboseWidget


class Controller:
    def __init__(self, verbose_widget: VerboseWidget, list_widget: PostsWidget,
                 posts: List[fp.Post], actions: Deque[str]):
        self.verbose_widget = verbose_widget
        self.list_widget = list_widget
        self.posts = posts
        self.actions = actions

        self._container = _WidgetContainer(self)
        self._container.add(0, 0, list_widget)
        self._container.add(0, 0, verbose_widget)

    def loop(self):
        self._container.loop()

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


class _WidgetContainer(Dialog):
    def __init__(self, controller: Controller):
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
