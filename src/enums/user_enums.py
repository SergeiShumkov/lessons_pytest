from enum import Enum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
