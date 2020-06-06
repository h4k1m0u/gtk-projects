import vlc
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(150, 100)

        # header bar with title and close button
        self.headerbar = Gtk.HeaderBar(title='Moussi9a')
        self.headerbar.set_show_close_button(True)
        self.set_titlebar(self.headerbar)

        # opened song in vlc player & its filename
        self.player = vlc.MediaPlayer()
        self.filename = ''

        # main layout
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        self.add(box)

        # toolbar with open button
        toolbar = Gtk.Toolbar()
        toolbar.set_style(Gtk.ToolbarStyle.ICONS)
        button_open = Gtk.ToolButton(Gtk.STOCK_OPEN)
        toolbar.insert(button_open, 0)
        box.pack_start(toolbar, False, False, 0)

        # buttons container
        grid_buttons = Gtk.Box()
        box.pack_start(grid_buttons, False, False, 0)

        # icons & images
        icon_play = Gio.ThemedIcon(name='media-playback-start-symbolic')
        icon_pause = Gio.ThemedIcon(name='media-playback-pause-symbolic')
        self.image_play = Gtk.Image.new_from_gicon(
            icon_play, Gtk.IconSize.BUTTON)
        self.image_pause = Gtk.Image.new_from_gicon(
            icon_pause, Gtk.IconSize.BUTTON)

        # play/pause buttons
        self.button_play_pause = Gtk.ToggleButton()
        self.button_play_pause.set_image(self.image_play)
        grid_buttons.pack_start(self.button_play_pause, False, False, 0)

        # attach signals to their handlers
        self.connect('destroy', self.on_destroy)
        self.button_play_pause.connect('toggled', self.on_play_pause)
        button_open.connect('clicked', self.on_open)

    def on_destroy(self, widget):
        Gtk.main_quit()

    def on_play_pause(self, widget):
        # no song is currently opened
        if self.player.get_media() is None:
            self.button_play_pause.set_active(False)
        else:
            if widget.get_active():
                self.player.play()
                widget.set_image(self.image_pause)
            else:
                self.player.pause()
                widget.set_image(self.image_play)

    def on_open(self, widget):
        # stop currently played song if opened
        if self.player.get_media() is not None:
            self.player.stop()
            self.button_play_pause.set_image(self.image_play)
            self.button_play_pause.set_active(False)

        # file by extension
        filter_mp3 = Gtk.FileFilter()
        filter_mp3.set_name('MP3 files')
        filter_mp3.add_mime_type('audio/mpeg')

        # open file dialog
        dialog = Gtk.FileChooserDialog(
            'Choose an audio file',
            self,
            Gtk.FileChooserAction.OPEN,
            (
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OK,
                Gtk.ResponseType.OK
            )
        )
        dialog.set_filter(filter_mp3)
        response = dialog.run()

        # get file name & destroy dialog
        if response == Gtk.ResponseType.OK:
            self.filename = dialog.get_filename()
        dialog.destroy()

        # load mp3 song
        self.player.set_mrl(self.filename)
        self.headerbar.set_subtitle(self.filename)


if __name__ == '__main__':
    # window & its main loop
    win = MyWindow()
    win.show_all()
    Gtk.main()
