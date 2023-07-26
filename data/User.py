from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str
