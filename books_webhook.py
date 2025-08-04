from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/book-search', methods=['POST'])
def book_search():
    user_input = request.json.get("query", "")
    url = f"https://www.googleapis.com/books/v1/volumes?q={user_input}"
    res = requests.get(url).json()

    books = []
    for item in res.get("items", [])[:3]:  # take top 3 books
        info = item.get("volumeInfo", {})
        books.append({
            "title": info.get("title", "No title"),
            "authors": info.get("authors", ["Unknown"])[0],
            "description": info.get("description", "No description")
        })

    return jsonify(books)

if __name__ == '__main__':
    app.run(port=5000)
