from sqlalchemy import create_engine
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


# connect to sqlite database file
engine = create_engine('sqlite:///database.db')


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

        # layout container
        self.box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # button & its click event
        self.button = Gtk.Button(label='Click here')
        self.button.connect('clicked', self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        # label
        self.label = Gtk.Label(label='My label')
        self.box.pack_start(self.label, True, True, 0)

    def on_button_clicked(self, widget):
        print('Button clicked!')


# window & its main loop
win = MyWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
