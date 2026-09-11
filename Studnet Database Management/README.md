# Student Management API

API quản lý sinh viên sử dụng FastAPI, SQLAlchemy và MySQL.

## 1. Công nghệ

* Python
* FastAPI
* SQLAlchemy
* MySQL
* PyMySQL
* Pydantic
* Pytest

## 2. Cấu trúc project

```text
student-management-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── students.py
│       └── health.py
│
├── tests/
│   └── test_students.py
│
├── sql/
│   └── student_management.sql
│
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

## 3. Trách nhiệm từng module

### `main.py`

Khởi tạo FastAPI và đăng ký các router.

### `database.py`

Quản lý kết nối MySQL và SQLAlchemy Session.

### `models.py`

Khai báo model `Student` tương ứng với bảng `students`.

### `schemas.py`

Validation dữ liệu request và định nghĩa response.

### `crud.py`

Chứa nghiệp vụ CRUD, search, filter và pagination.

### `routers/students.py`

Cung cấp các API quản lý sinh viên.

### `routers/health.py`

Kiểm tra trạng thái API và kết nối MySQL.

### `tests/test_students.py`

Chứa 12 test case kiểm tra API.

### `sql/student_management.sql`

Tạo database, bảng `students` và dữ liệu mẫu.

## 4. Cài đặt

Tạo virtual environment:

```bash
python -m venv .venv
```

Kích hoạt trên Windows:

```bash
.venv\Scripts\activate
```

Cài thư viện:

```bash
pip install -r requirements.txt
```

## 5. Cấu hình MySQL

Tạo database bằng file:

```text
sql/student_management.sql
```

Có thể mở file bằng MySQL Workbench và chạy toàn bộ SQL.

## 6. Cấu hình `.env`

Copy:

```text
.env.example
```

thành:

```text
.env
```

Ví dụ:

```env
DATABASE_URL=mysql+pymysql://root:123456@localhost:3306/student_management
```

Thay `123456` bằng password MySQL thực tế.

## 7. Chạy API

```bash
uvicorn app.main:app --reload
```

API chạy tại:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## 8. Các endpoint

| Method | Endpoint           | Chức năng                |
| ------ | ------------------ | ------------------------ |
| GET    | `/health`          | Health check             |
| GET    | `/students`        | Danh sách sinh viên      |
| GET    | `/students/search` | Search/filter/pagination |
| GET    | `/students/{id}`   | Chi tiết sinh viên       |
| POST   | `/students`        | Tạo sinh viên            |
| PUT    | `/students/{id}`   | Cập nhật toàn bộ         |
| PATCH  | `/students/{id}`   | Cập nhật một phần        |
| DELETE | `/students/{id}`   | Xóa sinh viên            |

## 9. Search, filter và pagination

Ví dụ:

```text
GET /students/search?keyword=An&min_age=18&max_age=25&is_active=true&page=1&page_size=10
```

Các tham số:

* `keyword`: tìm theo tên hoặc email
* `min_age`: tuổi nhỏ nhất
* `max_age`: tuổi lớn nhất
* `is_active`: trạng thái hoạt động
* `page`: số trang
* `page_size`: số bản ghi mỗi trang

## 10. Validation

API kiểm tra:

* Tên không được rỗng
* Email phải đúng định dạng
* Email không được trùng
* Số điện thoại không được trùng
* Password tối thiểu 6 ký tự
* Age từ 1 đến 120
* Page phải lớn hơn hoặc bằng 1
* Page size từ 1 đến 100
* `min_age` không được lớn hơn `max_age`

## 11. Test

Chạy:

```bash
pytest -v
```

Project có 12 test case kiểm tra:

1. Health check
2. Lấy danh sách
3. Lấy student theo ID
4. Student không tồn tại
5. Tạo student
6. Email bị trùng
7. Validation dữ liệu
8. PUT
9. PATCH
10. DELETE
11. Search/filter/pagination
12. Pagination không hợp lệ

## 12. Lưu ý

File `.env` không được commit lên Git vì có thông tin kết nối database.

Đối với project thực tế, password của student cần được hash trước khi lưu vào database.
