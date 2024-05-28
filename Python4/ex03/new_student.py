import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''generate a randome 15 lowercase character'''
    return "".join(random.choices(string.ascii_lowercase, k=15))

# # attemp 1
# @dataclass
# class Student:
#     '''variables of to instantiate'''
#     # name : str = field(kw_only = "name")
#     # surname : str = field(kw_only = "surname")
#     # name : str = field(metadata={"kw_only": "name"})
#     # surname : str = field(metadata={"kw_only": "surname"})
#     name: str
#     surname: str
#     active: bool = True
#     login: str = field(init=False)
#     # id : str = generate_id()
#     id: str = field(default_factory=generate_id, init=False)

#     def __post_init__(self):
#         self.login = self.name[0] + self.surname
# #  by default things are in fixed order...


# final
@dataclass
class Student:
    '''variables of to instantiate'''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname

# #  a better way to look at it
# @dataclass
# class Student:
#     '''variables of to instantiate'''
#     name: str = field(init=True)
#     surname: str = field(init=True)
#     active: bool = field(init=True, default=True)
#     login: str = field(init=False)
#     id: str = field(default_factory=generate_id, init=False)

#     def __post_init__(self):
#         self.login = self.name[0] + self.surname
