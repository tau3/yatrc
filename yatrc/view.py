from typing import Deque, List

from picotui.defs import (C_B_WHITE, C_BLACK, C_GRAY, C_GREEN, C_WHITE,
                          KEY_ENTER)
from picotui.screen import Screen
from picotui.widgets import WListBox
from picotui.editorext import Viewer


# pylint: disable=too-many-ancestors
class VerboseWidget(Viewer):
    def __init__(self):
        width, height = Screen.screen_size()
        super().__init__(0, 0, width, height)
        self.is_visible = False
        self.w = width  # pylint: disable=invalid-name
        self.h = height  # pylint: disable=invalid-name

    def redraw(self):
        if self.is_visible:
            super().redraw()


class PostsWidget(WListBox):
    def __init__(self, items: List[str], actions: Deque, is_visible=True):
        width, height = Screen.screen_size()
        super().__init__(width, height, items)
        default_style = (C_B_WHITE, C_GRAY)
        self.styles = [default_style] * len(items)
        self.is_visible = is_visible
        self.actions = actions

    def redraw(self):
        if self.is_visible:
            super().redraw()

    def show_line(self, line, i):
        hlite = self.cur_line == i
        if hlite:
            if self.focus:
                self.attr_color(C_WHITE, C_GREEN)
            else:
                self.attr_color(C_BLACK, C_GREEN)
        if i != -1:
            if not hlite:
                self.attr_color(*self.styles[i])
            line = self.render_line(line)[:self.width]
            self.wr(line)
        self.clear_num_pos(self.width - len(line))
        self.attr_reset()

    def handle_key(self, key):
        if key == KEY_ENTER:
            self.styles[self.cur_line] = (C_BLACK, C_GRAY)
            self.actions.append('verbose')
        return super().handle_key(key)
