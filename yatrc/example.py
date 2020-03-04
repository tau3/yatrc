from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import Dialog, WMultiEntry
from posts_widget import PostsWidget, VerboseWidget
import parser

def main():
    posts = parser.load_feed("https://www.opennet.ru/opennews/opennews_all_utf.rss")
    
    with Context():
        Screen.cls()
        Screen.attr_reset()
        w, h = Screen.screen_size()
        dialog = Dialog(0, 0, w, h, "foo")
        
        list_widget = PostsWidget(w, h, [post.list_view() for post in posts])
        list_widget.visible = True

        verbose_widget = VerboseWidget(w, h, ["hello", "world"])

        dialog.add(0, 0, list_widget) 
        dialog.add(0, 0, verbose_widget) 
        # dialog.redraw()
        dialog.loop()


if __name__ == "__main__":
    main()
