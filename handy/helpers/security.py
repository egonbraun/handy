from random import choice
from string import ascii_letters, digits


DEFAULT_PASSWORD_LENGTH: int = 25


def generate_password(length: int = DEFAULT_PASSWORD_LENGTH) -> str:
    return "".join(choice(ascii_letters + digits) for _ in range(length))
