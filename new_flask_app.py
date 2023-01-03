import connexion
import json
from flask import Flask, jsonify
import os

app = connexion.App(__name__)

@app.route("/")
def home():
    return "hello there"

@app.route('/books')
def books():
    books_list = [
        {
            "title": "Lord of the rings",
            "author": "J.R.R. Tolkien",
            "timestamp": "1954-07-29 00:00:00"
        },
        {
            "title": "Harry Potter and the goblet of fire",
            "author": "J.K. Rowling",
            "timestamp": "2000-07-08 00:00:00"
        },
        {
            "title": "I Heard You Paint Houses",
            "author": "Charles Brandt",
            "timestamp": "2004-01-01 00:00:00"
        },
        {
            "title": "Before caffe gets cold",
            "author": "Toshikazu Kawaguchi",
            "timestamp": "2015-12-01 00:00:00"
        }
    ]
    return jsonify(books_list), 200

if __name__ == "__main__":
    app.add_api('my_api.yaml')
    port = int(os.environ.get('PORT', 5001))
    app.run(port=port, host='0.0.0.0')