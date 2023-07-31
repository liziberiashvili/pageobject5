from dataclasses import dataclass


@dataclass
class UsersPersonalDetails:
    firstname: str
    surname: str
    street: str
    zipcode: int
    city: str
