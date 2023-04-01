import connexion
import json
from flask import Flask, jsonify
import os
from datetime import datetime
import pytz

# create timezone object for Poland
poland_tz = pytz.timezone("Europe/Warsaw")


app = connexion.App(__name__)

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
    return jsonify(books_list), 200

def books_post(book):
    title = book["title"]
    author = book["author"]
    book["timestamp"] = datetime.now(poland_tz)
    books_list.append(book)
    return jsonify(books_list), 200

def books_id_get(id):
    if id >= len(books_list):
        return {'error': 'Book not found'}, 404
    if id < 0:
        return {'error': 'Book not found'}, 404
    book = books_list[id]
    return jsonify(book), 200

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
    list_of_authors=[]
    for book in books_list:
        list_of_authors.append(book["author"])
    return jsonify(list_of_authors), 200

if __name__ == "__main__":
    app.add_api('my_api.yaml')
    port = int(os.environ.get('PORT', 5001))
    app.run(port=port, host='0.0.0.0')