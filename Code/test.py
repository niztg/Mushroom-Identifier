from Notes.Modules.classes import Note
from Accounts.Modules.classes import Account

from datetime import datetime

dob = datetime.strptime("August 21 2006", "%B %d %Y")
acc = Account('nansa1', 'password', 'email@email.com', dob, 12345)

note = Note.create_note(author=acc, content="Hello!")
print(note)

note.edit_note(note.content, 'Goodbye!')
print(note)
print(note._date)