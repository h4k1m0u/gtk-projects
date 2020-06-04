import vlc
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Moussi9a')
        self.set_default_size(150, 100)
        # self.set_border_width(10)

        # buttons container
        grid_buttons = Gtk.Grid(row_spacing=10, column_spacing=10, margin=10)
        self.add(grid_buttons)

        # icons & images
        icon_play = Gio.ThemedIcon(name='media-playback-start-symbolic')
        icon_pause = Gio.ThemedIcon(name='media-playback-pause-symbolic')
        self.image_play = Gtk.Image.new_from_gicon(
            icon_play, Gtk.IconSize.BUTTON)
        self.image_pause = Gtk.Image.new_from_gicon(
            icon_pause, Gtk.IconSize.BUTTON)

        # play/pause buttons
        button_play_pause = Gtk.ToggleButton()
        button_play_pause.set_image(self.image_play)
        grid_buttons.attach(button_play_pause, 0, 0, 1, 1)

        # load mp3 song
        self.song = vlc.MediaPlayer('music.mp3')

        # attach signals to their handlers
        self.connect('destroy', self.on_destroy)
        button_play_pause.connect('toggled', self.on_play_pause)

    def on_destroy(self, widget):
        Gtk.main_quit()

    def on_play_pause(self, widget):
        if widget.get_active():
            self.song.play()
            widget.set_image(self.image_pause)
        else:
            self.song.pause()
            widget.set_image(self.image_play)


if __name__ == '__main__':
    # window & its main loop
    win = MyWindow()
    win.show_all()
    Gtk.main()
