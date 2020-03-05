from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import Dialog
from yatrc.widgets import PostsWidget, VerboseWidget
import yatrc.feed_parser as fp


def main() -> None:
    posts = fp.load_feed(
        "https://www.opennet.ru/opennews/opennews_all_utf.rss")

    with Context():
        Screen.cls()
        Screen.attr_reset()
        width, height = Screen.screen_size()
        dialog = Dialog(0, 0, width, height, "foo")

        list_widget = PostsWidget(width, height,
                                  [post.list_view() for post in posts])
        list_widget.visible = True

        verbose_widget = VerboseWidget(width, height, ["hello", "world"])

        dialog.add(0, 0, list_widget)
        dialog.add(0, 0, verbose_widget)
        # dialog.redraw()
        dialog.loop()


if __name__ == "__main__":
    main()
