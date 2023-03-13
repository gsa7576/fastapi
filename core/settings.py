from passlib.context import CryptContext
PWD_CONTENT = CryptContext(schemes=['bcrypt'], deprecated='auto')