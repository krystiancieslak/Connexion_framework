from datetime import datetime
from config import db, ma

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(32))
    title = db.Column(db.String(32), unique=True)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session

book_schema = BookSchema()
books_schema = BookSchema(many=True)