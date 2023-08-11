from models import Book, BookSchema
import json
from flask import jsonify
import os
from datetime import datetime
import pytz
from config import db, poland_tz, app, connex_app

with app.app_context():
    db.create_all()

with app.app_context():
    if not Book.query.first():
        with open('books.json', 'r') as file:
            books_data = json.load(file)

        for book_data in books_data:
            timestamp_str = book_data['timestamp']
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            book = Book(name=book_data['name'], surname=book_data['surname'], title=book_data['title'], timestamp=timestamp)
            db.session.add(book)
        db.session.commit()

books_list = [
    {
        "title": "Lord of the rings",
        "author": "J.R.R. Tolkien",
        "timestamp": datetime.now(poland_tz)
    },
    {
        "title": "Harry Potter and the goblet of fire",
        "author": "J.K. Rowling",
        "timestamp": datetime.now(poland_tz)
    },
    {
        "title": "I Heard You Paint Houses",
        "author": "Charles Brandt",
        "timestamp": datetime.now(poland_tz)
    },
    {
        "title": "Before caffe gets cold",
        "author": "Toshikazu Kawaguchi",
        "timestamp": datetime.now(poland_tz)
    }
]


def home():
    return "hello there"

def books_get():
    books = Book.query.all()
    books_schema = BookSchema(many=True)
    return jsonify(books_schema.dump(books))

def books_post(body):
    title = body.get("title")
    name = body.get("name")
    surname = body.get("surname")

    if not title or not name or not surname:
        return jsonify({"message": "Invalid input"}), 400

    last_book = Book.query.order_by(Book.id.desc()).first()
    next_id = last_book.id + 1 if last_book else 1

    new_book = Book(id=next_id, title=title, name=name, surname=surname, timestamp=datetime.now(poland_tz))

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"id": new_book.id}), 201

def books_id_get(id):
    book = Book.query.get(id)
    
    if book:
        book_schema = BookSchema()
        return jsonify(book_schema.dump(book))
    else:
        return jsonify({"message": "Book not found"}), 404

def books_id_put(id, data):
    if id >= len(books_list):
        return {'error': 'Book not found'}, 404
    if id < 0:
        return {'error': 'Book not found'}, 404
    title = data["title"]
    author = data["author"]
    data["timestamp"] = datetime.now(poland_tz)
    books_list[id]['title'] = data['title']
    books_list[id]['author'] = data['author']
    return jsonify(books_list[id]), 200

def books_id_delete(id):
    if id >= len(books_list):
        return {'error': 'Book not found'}, 404
    if id < 0:
        return {'error': 'Book not found'}, 404
    del books_list[id]
    return 200

def authors():
    books = Book.query.all()

    authors_list = set()
    for book in books:
        author_name = f"{book.name} {book.surname}"
        authors_list.add(author_name)

    sorted_authors = sorted(list(authors_list))
    
    return jsonify(sorted_authors)

if __name__ == "__main__":
    connex_app.add_api('my_api.yaml')  # Use connex_app to add API
    port = int(os.environ.get('PORT', 5001))
    connex_app.run(port=port, host='0.0.0.0')  # Use connex_app to run the application