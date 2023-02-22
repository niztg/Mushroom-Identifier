__all__ = (
    'InvalidDateOfBirth',
    'NotOldEnough',
    'UsernameNotRightLength',
    "EmailNotProper"
)

class InvalidDateOfBirth(Exception):
    def __repr__(self):
        return "Date of birth must be entered in the following format: YYYY-MM-DD"

class NotOldEnough(Exception):
    def __repr__(self):
        return "You are not old enough!"

class UsernameNotRightLength(Exception):
    def __repr__(self):
        return "Username and display name must be between 6 and 20 characters!"

class EmailNotProper(Exception):
    def __repr__(self):
        return "Please enter a valid email"