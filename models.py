from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String())
    name = db.Column(db.String())
    author = db.Column(db.String())
    pages = db.Column(db.Integer())
    year = db.Column(db.Integer())
    created_at = db.Column(db.Date())

    def __init__(self, isbn, name, author, pages, year, created_at):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.pages = pages
        self.year = year
        self.created_at = created_at

    def __repr__(self):
        return f"{self.isbn}:{self.name}:{self.author}:{self.pages}:{self.year}"