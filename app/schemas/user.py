from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    patronymic: str | None = None
    email: EmailStr
    password: str
    password_confirm: str


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    patronymic: str | None = None
    email: str
    is_active: bool
    role_id: int

    model_config = {"from_attributes": True}
