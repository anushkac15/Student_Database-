CREATE DATABASE IF NOT EXISTS student_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE student_management;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) UNIQUE,
    age INT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students
(name, email, password, phone, age, is_active)
VALUES
('Nguyen Van An', 'an@gmail.com', '123456', '0900000001', 20, TRUE),
('Tran Thi Binh', 'binh@gmail.com', '123456', '0900000002', 21, TRUE),
('Le Van Cuong', 'cuong@gmail.com', '123456', '0900000003', 22, TRUE),
('Pham Thi Dung', 'dung@gmail.com', '123456', '0900000004', 19, TRUE),
('Hoang Van Em', 'em@gmail.com', '123456', '0900000005', 25, FALSE),
('Do Thi Hoa', 'hoa@gmail.com', '123456', '0900000006', 20, TRUE),
('Nguyen Van Long', 'long@gmail.com', '123456', '0900000007', 24, TRUE),
('Tran Van Minh', 'minh@gmail.com', '123456', '0900000008', 23, FALSE),
('Le Thi Nga', 'nga@gmail.com', '123456', '0900000009', 21, TRUE),
('Pham Van Nam', 'nam@gmail.com', '123456', '0900000010', 26, TRUE);