from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    pass

def verify_password(plain_password: str, hashed_password: str) -> bool:
    pass