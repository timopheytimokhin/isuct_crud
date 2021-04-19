-- Скрипт для создания таблицы книг

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR(255),
    name VARCHAR(255),
    author VARCHAR(255),
    pages INTEGER,
    year INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Скрипт для удаления таблицы книг
DROP TABLE books;