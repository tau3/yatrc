from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *


class MyListBox(WListBox):
    def __init__(self, width, height, items):
        super().__init__(width, height, items)
        self.default_style = (C_B_WHITE, C_GRAY)
        self.styles = [self.default_style] * len(items)

    def show_line(self, line, i):
        # self.attr_reset()
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
        return super().handle_key(key)

