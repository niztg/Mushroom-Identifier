"""
Where the note classes live.
all note functions written by: niz
"""

import sqlite3

from Accounts.Modules.classes import Account
from datetime import datetime
from .exceptions import NoteDoesntExist


class Note:
    """
    Defines the note class.
    Attributes:
        author: Account = The author of the note
        content: str = The content of the note
        date: datetime = Date the note was created
    """

    def __init__(self, author: Account, content: str, date: datetime):
        """
        Initializes the class
        """
        self._author = author
        self._content = content
        self._date = date

        self._conn = sqlite3.connect("Notes/Databases/notes.db")
        self._cursor = self._conn.cursor()

        sql = """ CREATE TABLE IF NOT EXISTS notes (
content TEXT,
author integer,
date DATETIME
);
"""
        self._cursor.execute(sql)

    def __repr__(self):
        """
        Displays information about the class
        Args:
            None
        Retuens:
            str
        """
        return f"Note written by {self._author._name} on {self._date}: {self.content}"

    @property
    def content(self):
        self._cursor.execute("SELECT content FROM notes WHERE author=? AND date=?", (self._author._id, self._date))
        return self._cursor.fetchone()[0]

    @classmethod
    def create_note(cls, author: Account, content: str):
        """
        Creates a note.
        :param author:
        :param content:
        :return:
        """
        current_date = datetime.now()
        # the UI will check if the note is too long,
        # it doesn't need to be built into the backend of the code directly

        obj = cls(author, content, current_date)

        args = (content, int(author._id), current_date)
        sql = "INSERT INTO notes (content, author, date) VALUES (?, ?, ?)"

        obj._cursor.execute(sql, args)

        return obj

    def edit_note(self, content: str, new_content: str):
        """
        Edits a note.
        :param content:
        :param new_content:
        :return:
        """
        self._cursor.execute("UPDATE notes SET content=? WHERE content=? AND author=?", (new_content, content, self._author._id))
