from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=255)
    phone: str | None = Field(default=None, max_length=20)
    age: int | None = Field(default=None, ge=1, le=120)
    is_active: bool = True


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=255)
    phone: str | None = Field(default=None, max_length=20)
    age: int | None = Field(default=None, ge=1, le=120)
    is_active: bool = True


class StudentPatch(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=6, max_length=255)
    phone: str | None = Field(default=None, max_length=20)
    age: int | None = Field(default=None, ge=1, le=120)
    is_active: bool | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None
    age: int | None
    is_active: bool
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class StudentListResponse(BaseModel):
    items: list[StudentResponse]
    page: int
    page_size: int
    total: int
    total_pages: int