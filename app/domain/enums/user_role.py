from enum import Enum


class RoleEnum(Enum):
    ROOT = 1
    ADMIN = 2
    EMPLOYEE = 3

    ALL = [ROOT, ADMIN, EMPLOYEE]


print(RoleEnum.ALL.value)
