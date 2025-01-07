from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for books
books = []

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    book = request.get_json()
    books.append(book)
    return jsonify({"message": "Book added successfully"}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    if 0 <= book_id < len(books):
        return jsonify(books[book_id])
    return jsonify({"error": "Book not found"}), 404

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if 0 <= book_id < len(books):
        book = request.get_json()
        books[book_id] = book
        return jsonify({"message": "Book updated successfully"})
    return jsonify({"error": "Book not found"}), 404

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if 0 <= book_id < len(books):
        books.pop(book_id)
        return jsonify({"message": "Book deleted successfully"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
