from pydantic import BaseModel, Field, EmailStr, root_validator
#https://github.com/ArtsemDev/bankapi
from ..


class RegisterForm(BaseModel):
    email: EmailStr = Field(
        title='User Email',
        description='User Unique Email'
    )
    username: str = Field(
        title='Username',
        description='Unique Username',
        max_length=128,
        min_length=2
    )
    password: str = Field(
        title='User Password',
        description='User Password',
        min_length=8,
        max_length=64,
        regex=r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})'
    )
    repeat_password: str = Field(
        title='Repeat Password',
        description='Repeat Password',
        min_length=8,
        max_length=64,
        regex=r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})'
    )

    @root_validator(pre=True)
    def validator(cls, values: dict) -> dict:
        if values.get('password') != values.get('repeat_password'):
            raise ValueError('пароли не совпадают')

        if values.get('username').lower() in values.get('password').lower():
            raise ValueError('имя пользователя не должно содержаться в пароле')

        if values.get('email').lower().split('@')[0] in values.get('password').lower():
            raise ValueError('почта не должна содержаться в пароле')

        return values

    class UserInfo(BaseModel):