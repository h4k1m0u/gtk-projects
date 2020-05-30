from models import Word
from datetime import datetime
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Hello world')

        # header bar with title and close button
        headerbar = Gtk.HeaderBar()
        headerbar.props.title = 'Tarjama'
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        # add/remove word buttons in headbar
        box_buttons_edit = Gtk.Box()
        box_buttons_edit.get_style_context().add_class('linked')
        headerbar.pack_start(box_buttons_edit)

        button_add = Gtk.Button()
        icon = Gio.ThemedIcon(name='list-add-symbolic')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button_add.add(image)
        box_buttons_edit.pack_start(button_add, True, True, 0)

        button_remove = Gtk.Button()
        icon = Gio.ThemedIcon(name='list-remove-symbolic')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button_remove.add(image)
        box_buttons_edit.pack_start(button_remove, True, True, 0)

        button_edit = Gtk.Button()
        icon = Gio.ThemedIcon(name='document-edit-symbolic')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button_edit.add(image)
        headerbar.pack_start(button_edit)

        # navigations buttons in headbar
        box_buttons_nav = Gtk.Box()
        box_buttons_nav.get_style_context().add_class('linked')
        headerbar.pack_end(box_buttons_nav)

        button_down = Gtk.Button()
        icon = Gio.ThemedIcon(name='go-down-symbolic')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button_down.add(image)
        box_buttons_nav.pack_start(button_down, True, True, 0)

        button_up = Gtk.Button()
        icon = Gio.ThemedIcon(name='go-up-symbolic')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button_up.add(image)
        box_buttons_nav.pack_start(button_up, True, True, 0)

        button_search = Gtk.Button()
        icon = Gio.ThemedIcon(name='edit-find-symbolic')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button_search.add(image)
        headerbar.pack_end(button_search)

        # load data from database
        self.show_words()

        # connect handler to buttons click events
        button_add.connect('clicked', self.add_word)
        button_remove.connect('clicked', self.remove_word)
        button_edit.connect('clicked', self.edit_word)
        button_down.connect('clicked', self.goto_next_word)
        button_up.connect('clicked', self.goto_previous_word)
        button_search.connect('clicked', self.search_word)

    def show_words(self):
        # load words from database
        words = Word.retrieve_all()

        # fill list model with words from database
        store = Gtk.ListStore(int, str, str, str)
        for word in words:
            store.append([word.id, word.word, word.translation,
                          word.date.strftime("%Y-%m-%d %H:%M:%S")])

        # add list view to window
        self.list = Gtk.TreeView(store)
        column_id = Gtk.TreeViewColumn(
            'Id', Gtk.CellRendererText(), text=0)
        self.list.append_column(column_id)
        column_word = Gtk.TreeViewColumn(
            'Word', Gtk.CellRendererText(), text=1)
        self.list.append_column(column_word)
        column_translation = Gtk.TreeViewColumn(
            'Translation', Gtk.CellRendererText(), text=2)
        self.list.append_column(column_translation)
        column_date = Gtk.TreeViewColumn(
            'Date', Gtk.CellRendererText(), text=3)
        self.list.append_column(column_date)
        self.add(self.list)

    def add_word(self, widget):
        # insert new word in database
        word = Word(word='test word', translation='test translation',
                    date=datetime.now())
        word_id = Word.insert(word)
        word = Word.retrieve_by_id(word_id)

        # add inserted word to list view
        store = self.list.get_model()
        store.append([word.id, word.word, word.translation,
                      word.date.strftime("%Y-%m-%d %H:%M:%S")])

    def remove_word(self, widget):
        # remove word from database
        store, iter_list = self.list.get_selection().get_selected()
        word_id = store[iter_list][0]
        Word.delete_by_id(word_id)

        # remove row from list view
        store.remove(iter_list)

    def edit_word(self, widget):
        # get selected row
        store, iter_list = self.list.get_selection().get_selected()
        word_id = store[iter_list][1]
        print('word id:', word_id)

    def goto_next_word(self, widget):
        # get selected row
        selection = self.list.get_selection()
        store, iter_list = selection.get_selected()

        # set cursor to next row or first if limit reached
        iter_list_first = store.get_iter_first()
        iter_list = store.iter_next(iter_list) or iter_list_first
        selection.select_iter(iter_list)

    def goto_previous_word(self, widget):
        # get selected row
        selection = self.list.get_selection()
        store, iter_list = selection.get_selected()

        # set cursor to previous row or last if limit reached
        iter_list_last = store.iter_nth_child(None, store.iter_n_children()-1)
        iter_list = store.iter_previous(iter_list) or iter_list_last
        selection.select_iter(iter_list)

    def search_word(self, widget):
        pass


if __name__ == '__main__':
    # window & its main loop
    win = MyWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
