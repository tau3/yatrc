from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import Dialog, WMultiEntry
from posts_widget import PostsWidget
import parser

def main():
    posts = parser.load_feed("https://www.opennet.ru/opennews/opennews_all_utf.rss")
    
    with Context():
        Screen.cls()
        Screen.attr_reset()
        w, h = Screen.screen_size()
        dialog = Dialog(0, 0, w, h, "foo")
        dialog.add(0, 0, PostsWidget(w, h, [post.list_view() for post in posts]))
        # dialog.add(0, 0, WMultiEntry(w, h, ["hello", "world"]))
        dialog.loop()


if __name__ == "__main__":
    main()
