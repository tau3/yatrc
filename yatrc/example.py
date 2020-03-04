from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import Dialog, WMultiEntry
from posts_widget import MyListBox

def main():
    with Context():
        Screen.cls()
        Screen.attr_reset()
        w, h = Screen.screen_size()
        dialog = Dialog(0, 0, w, h, 'foo')
        dialog.add(0, 0, MyListBox(w, h, ['foo', 'bar', 'baz']))
        dialog.add(0, 0, WMultiEntry(w,h,["hello", "world"]))
        dialog.loop()


if __name__ == '__main__':
    main()
