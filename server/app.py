from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Book, User, Review, Quote

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


@app.route('/')
def home():
    return ''

@app.route('/books', methods=['GET', 'POST'])
def book():
    books = Book.query.all()
    if request.method == 'GET':
        books_dict = [book.to_dict() for book in books]

        response = make_response(
            jsonify(books_dict),
            200
        )

        return response
    

    elif request.method == 'POST':

        try:
            new_book = Book(
                name = request.get_json()['name'],
                author = request.get_json()['author'],
                publishDate = request.get_json()['publishDate'],
                genre = request.get_json()['genre'],
                link = request.get_json()['link'],
                summary = request.get_json()['summary'],
                image = request.get_json()['image']
            )
            db.session.add(new_book)
            db.session.commit()

            response = make_response(
                jsonify(new_book.to_dict()),
                201
            )

        except ValueError:

            response = make_response(
                {"error": "validation errors"},
                400
            )
    return response

















































if __name__ == '__main__':
    app.run(port=5555, debug=True)
