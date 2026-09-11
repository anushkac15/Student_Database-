from math import ceil

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.models import Student
from app.schemas import (
    StudentCreate,
    StudentListResponse,
    StudentPatch,
    StudentResponse,
    StudentUpdate,
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def check_duplicate(
    db: Session,
    email: str | None = None,
    phone: str | None = None,
    student_id: int | None = None
):
    query = db.query(crud.Student) if False else None

    if email:
        existing = (
            db.query(Student)
            .filter(Student.email == email)
            .first()
        )

        if existing and existing.id != student_id:
            raise HTTPException(
                status_code=409,
                detail="Email đã tồn tại"
            )

    if phone:
        existing = (
            db.query(Student)
            .filter(Student.phone == phone)
            .first()
        )

        if existing and existing.id != student_id:
            raise HTTPException(
                status_code=409,
                detail="Số điện thoại đã tồn tại"
            )