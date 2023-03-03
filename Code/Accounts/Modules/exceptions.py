"""
Module which contains custom exceptions
"""
# written by: niz

__all__ = (
    'InvalidDateOfBirth',
    'NotOldEnough',
    'UsernameNotRightLength',
    "EmailNotProper"
)


class InvalidDateOfBirth(Exception):
    def __str__(self):
        return "Date of birth must be entered in the following format: YYYY-MM-DD"


class NotOldEnough(Exception):
    def __str__(self):
        return "You are not old enough!"


class UsernameNotRightLength(Exception):
    def __str__(self):
        return "Username and display name must be between 6 and 20 characters!"


class EmailNotProper(Exception):
    def __str__(self):
        return "Please enter a valid email"


class UsernameTaken(Exception):
    def __str__(self):
        return "This username has already been taken!"
