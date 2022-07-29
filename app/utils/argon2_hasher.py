from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from app.data import settings


class Argon2Hasher:
    def __init__(self) -> None:
        self.passwordHasher = PasswordHasher()
        self.pepper = settings.PEPPER

    def hash(self, plaintext: str) -> str:
        return self.passwordHasher.hash(f"{plaintext}:{self.pepper}")

    def verify(self, hash: str, plaintext: str) -> bool:
        try:
            peppered_password = f"{plaintext}:{self.pepper}"
            return self.passwordHasher.verify(hash, peppered_password)
        except VerifyMismatchError:
            return False
