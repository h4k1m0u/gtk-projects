import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# same dialog used for adding new word & editing existing words
class Dialog(Gtk.Dialog):
    def __init__(self, parent, word='', translation=''):
        super().__init__('Add new word', parent, 0, (
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK
        ))
        self.set_default_size(150, 100)

        # dialog layout
        grid = Gtk.Grid(row_spacing=10, column_spacing=10, margin=10)

        # add form entries to dialog
        label_word = Gtk.Label('Word', halign=Gtk.Align.START)
        self.entry_word = Gtk.Entry(hexpand=True, text=word)
        label_translation = Gtk.Label('Translation', halign=Gtk.Align.START)
        self.entry_translation = Gtk.Entry(hexpand=True, text=translation)
        grid.attach(label_word, 0, 0, 1, 1)
        grid.attach(self.entry_word, 1, 0, 1, 1)
        grid.attach(label_translation, 0, 1, 1, 1)
        grid.attach(self.entry_translation, 1, 1, 1, 1)

        # show dialog children (form entries)
        box = self.get_content_area()
        box.pack_start(grid, True, True, 0)
        self.show_all()

        # connect action widget clicked signal
        self.connect('response', self.on_response)

    def on_response(self, widget, response_id):
        # save entered word & translation on button clicked
        if response_id == Gtk.ResponseType.OK:
            self.word = self.entry_word.get_text()
            self.translation = self.entry_translation.get_text()
