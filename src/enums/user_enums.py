from enum import Enum

from src.baseclasses.pyenum import PyEnum

class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    DELETED = "DELETED"
    BANNED = "BANNED"
    MERGED ="MERGED"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
