"""
Note related functions
"""

import sqlite3

from Accounts.Modules.classes import Account
from datetime import datetime

conn = sqlite3.connect('Databases/notes.db')
cursor = conn.cursor()

def create_note(author: Account, content: str):
    ...
    current_date = str(datetime.now())
    cursor.execute("INSERT INTO notes VALUES (?, ?, ?)", author, content, current_date)
