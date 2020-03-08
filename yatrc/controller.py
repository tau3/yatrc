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

        width, height = Screen.screen_size()
        self._container = Dialog(x=0, y=0, w=width, h=height)
        self._container.add(x=0, y=0, widget=list_widget)
        self._container.add(x=0, y=0, widget=verbose_widget)
        self._container.change_focus(self.list_widget)

    def loop(self):
        while True:
            if self.handle_action():
                self._container.redraw()
            key = self._container.focus_w.get_input()
            res = self._container.focus_w.handle_input(key)

            if res is not None and res is not True:
                return res

    def handle_action(self):
        if self.actions:
            action = self.actions.pop()
            if action == 'verbose':
                index = self.list_widget.cur_line
                post = self.posts[index]
                self.verbose_widget.set_lines(post.verbose_view())
                self.verbose_widget.is_visible = True
                self.list_widget.is_visible = False
                self._container.change_focus(self.verbose_widget)
            elif action == 'list':
                self.verbose_widget.is_visible = False
                self.list_widget.is_visible = True
                self._container.change_focus(self.list_widget)
            return True
        return False
