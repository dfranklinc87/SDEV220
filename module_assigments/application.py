from flask import Flask, request, jsonify



app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

db = SQLAlchemy(app)

class Book(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      book_name = db.Column(db.String(80), unique=True, nullable=False)
      author = db.Column(db.String(120))
      publisher = db.Column(db.String(120))
      
  
      def __repr__(self):
           return f"{self.book_name} - {self.author} - {self.publisher}"
      
      def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher
        }


with app.app_context():
     db.create_all()

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    new_book = Book(
        id=data.get("id"),
        book_name=data.get("book_name"),
        author=data.get("author"),
        publisher=data.get("publisher")
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
    book.book_name = data.get("book_name", book.book_name)
    book.author = data.get("author", book.author)
    book.publisher = data.get("publisher", book.publisher)

    db.session.commit()
    return jsonify(book.to_dict()), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"}), 200




@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books]), 200




@app.route('/')
def index():
    return 'Hello!'



if __name__ == "__main__":
    app.run(debug=True)
