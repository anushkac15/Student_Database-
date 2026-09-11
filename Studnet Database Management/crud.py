from sqlalchemy import or_
from sqlalchemy.orm import Session

from models import Student
from schemas import StudentCreate, StudentPatch, StudentUpdate


def get_students(
    db: Session,
    page: int = 1,
    page_size: int = 10
):
    offset = (page - 1) * page_size

    total = db.query(Student).count()

    students = (
        db.query(Student)
        .offset(offset)
        .limit(page_size)
        .all()
    )

    return students, total


def get_student_info(
    db: Session,
    student_id: int
):
    return (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )


def get_student_by_email(
    db: Session,
    student_email: str
):
    return (
        db.query(Student)
        .filter(Student.email == student_email)
        .first()
    )


def get_student_by_phone(
    db: Session,
    student_phone: str
):
    return (
        db.query(Student)
        .filter(Student.phone == student_phone)
        .first()
    )


def add_student(
    db: Session,
    student: StudentCreate
):
    new_student = Student(
        name=student.name,
        email=student.email,
        password=student.password,
        phone=student.phone,
        age=student.age,
        is_active=student.is_active
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def search_students(
    db: Session,
    keyword: str | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    is_active: bool | None = None,
    page: int = 1,
    page_size: int = 10
):
    query = db.query(Student)

    if keyword:
        keyword = f"%{keyword}%"

        query = query.filter(
            or_(
                Student.name.ilike(keyword),
                Student.email.ilike(keyword)
            )
        )

    if min_age is not None:
        query = query.filter(
            Student.age >= min_age
        )

    if max_age is not None:
        query = query.filter(
            Student.age <= max_age
        )

    if is_active is not None:
        query = query.filter(
            Student.is_active == is_active
        )

    total = query.count()

    offset = (page - 1) * page_size

    students = (
        query
        .offset(offset)
        .limit(page_size)
        .all()
    )

    return students, total


def update_student(
    db: Session,
    db_student: Student,
    student: StudentUpdate
):
    db_student.name = student.name
    db_student.email = student.email
    db_student.password = student.password
    db_student.phone = student.phone
    db_student.age = student.age
    db_student.is_active = student.is_active

    db.commit()
    db.refresh(db_student)

    return db_student


def patch_student(
    db: Session,
    db_student: Student,
    student: StudentPatch
):
    data = student.model_dump(
        exclude_unset=True
    )

    for field, value in data.items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(
    db: Session,
    db_student: Student
):
    db.delete(db_student)
    db.commit()