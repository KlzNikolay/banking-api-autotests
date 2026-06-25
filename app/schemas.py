from pydantic import BaseModel


class UserCreate(BaseModel):
    full_name: str
    phone: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    phone: str

    class Config:
        from_attributes = True