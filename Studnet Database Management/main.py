from fastapi import FastAPI

from Bai12.app.health import router as health_router
from Bai12.app.students import router as student_router

app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

app.include_router(student_router)
app.include_router(health_router)