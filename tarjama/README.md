# Tutorials
-----------
- Documentation of [Python GTK+ 3][gi].
- Gnome documentation of [PyGTK 2][pygtk2].
- Gnome documentation of [PyGio][pygio].
- Source code of [Gajim][gajim] (uses Python GTK+ 3).

[gi]: https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
[pygtk2]: https://developer.gnome.org/pygtk/2.24/
[pygio]: https://developer.gnome.org/pygobject/stable/gio-class-reference.html
[gajim]: https://github.com/gajim/gajim/blob/master/gajim/gtk

# Gnome icons
-------------

```bash
sudo apt-get install gtk-3-examples
gtk3-icon-browser
```

# Arabic-support from terminal
----------------------------------
The terminal of Ubuntu 18.04 doesn't support Arabic by default. [bicon][bicon] needs to be installed which itself depends on [fribidi][fribidi]. Both can be installed from source with:

```bash
./autogen.sh
./configure
make && sudo make install
```

After the installation, support for Arabic can be enabled by running `bicon` from the terminal.

[bicon]: https://github.com/behdad/bicon
[fribidi]: https://github.com/fribidi/fribidi


# SQLite database
-----------------
## Prerequisites
SQLite and SQLAlchemy

```bash
sudo apt install sqlite3
pip install sqlalchemy
```

## Database
The database table is created automatically if it doesn't exist.

```bash
$ sqlite3 database.db

sqlite> SELECT * FROM words;
```

# License
---------
According to [this source][3], GTK can be used for commercial applications for free (unlike Qt):
> The licensing terms for GTK, the GNU LGPL , allow it to be used by all developers, including those developing proprietary software, without any license fees or royalties.

According to [this source][4], LGPL doesn't force you to release the source code when distributing binaries (as long as it's dynamically linked):
> LGPL allows you to use and distribute the open source software with your application without releasing the source code for your application.

If your program links to a GPL library then your program also comes under the GPL ([source][5]). That's not the case with LGPL with non-derivative works ([source][6]):
> Applications which link to LGPL libraries need not be released under the LGPL.

When a LGPL-licensed library is modified, only the source code of the library needs to be distributed not the application ([source][7]):

> LGPL requires modifications to the library source code to be distributed to anybody that used your code. It does not require that your code, which uses the library, be open-sourced and released under the same license.

[3]: https://gitlab.gnome.org/GNOME/gtk/blob/master/README.md
[4]: https://stackoverflow.com/a/1114054/2228912
[5]: https://opensource.stackexchange.com/a/415
[6]: https://www.gnu.org/licenses/lgpl-java.en.html
[7]: https://softwareengineering.stackexchange.com/a/136703/315516
