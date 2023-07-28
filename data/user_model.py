from dataclasses import dataclass


@dataclass
class Registration:
    password: str
    email: str
    domain: str
