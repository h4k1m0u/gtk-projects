# Tarjama
GUI application made with PyGTK 3.0 showing on a grid words and their corresponding translations saved in an SQLite database, with the possibility to add/delete/edit them.

## Functionalities
- Load words and their translations from a SQLite database. 
- Show words and their translations on a table grid.
- Possibility to add/remove/edit words and their translations on the table.


# SQLite database
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


# Arabic-support from terminal
The terminal of Ubuntu 18.04 doesn't support Arabic by default. [bicon][bicon] needs to be installed which itself depends on [fribidi][fribidi]. Both can be installed from source with:

```bash
./autogen.sh
./configure
make && sudo make install
```

After the installation, support for Arabic can be enabled by running `bicon` from the terminal.

[bicon]: https://github.com/behdad/bicon
[fribidi]: https://github.com/fribidi/fribidi
