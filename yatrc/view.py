from typing import Deque, List

from picotui.defs import (C_B_WHITE, C_BLACK, C_GRAY, C_GREEN, C_WHITE,
                          KEY_ENTER)
from picotui.screen import Screen
from picotui.widgets import WListBox
from picotui.editorext import Viewer
from yatrc.model import Post


# pylint: disable=too-many-ancestors
class VerboseWidget(Viewer):
    def __init__(self, actions: Deque):
        width, height = Screen.screen_size()
        super().__init__(0, 0, width, height)
        self.is_visible = False
        self.actions = actions
        self.w = width  # pylint: disable=invalid-name
        self.h = height  # pylint: disable=invalid-name

    def redraw(self):
        if self.is_visible:
            super().redraw()

    def handle_key(self, key):
        if key == KEY_ENTER:
            self.actions.append('list')
            return None
        return super().handle_key(key)

    def set_post(self, post: Post):
        self.set_lines(post.verbose_view())
        self.top_line = 0
        self.cur_line = 0
        self.row = 0
        self.adjust_cursor_eol()
        self.redraw()

    def set_lines(self, lines: List[str]):
        result = []
        for line in lines:
            if len(line) <= self.width:
                result.append(line)
            else:
                chunked = _chunks(line, self.width)
                result += chunked
        super().set_lines(result)


def _chunks(seq, length):
    for i in range(0, len(seq), length):
        yield seq[i:i + length]


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
