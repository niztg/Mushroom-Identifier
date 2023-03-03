"""
Custom exceptions for note-specific functions.
"""


class NoteTooLong(Exception):
    def __repr__(self):
        return "Your note is too long! The maximum character limit is 140."

class NoteDoesntExist(Exception):
    def __repr__(self):
        return "This note does not exist!"
