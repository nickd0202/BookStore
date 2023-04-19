from flask import Flask, make_response, request, jsonify, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError

from models import db, Book, User, Review, Quote

from config import app, db, api



class Signup(Resource):
    
    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')
        age= request_json.get('age')

        user = User(
            username=username,
            age=age
        )

        # the setter will encrypt this
        user.password_hash = password

        print('first')

        try:

            print('here!')

            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            print(user.to_dict())

            return user.to_dict(), 201

        except IntegrityError:

            print('no, here!')
            
            return {'error': '422 Unprocessable Entity'}, 422

class CheckSession(Resource):
    
    def get(self):

        if session.get('user_id'):

            user = User.query.filter(User.id == session['user_id']).first()

            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Login(Resource):
    
    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')

        user = User.query.filter(User.username == username).first()

        if user:
            if user.authenticate(password):

                session['user_id'] = user.id
                return user.to_dict(), 200

        return {'error': 'I believe you put in the wrong username or password, but you can always make a new account!'}, 401

class Logout(Resource):
    
    def delete(self):
        
        if session.get('user_id'):
            
            session['user_id'] = None
            
            return {}, 204
        
        return {'error': '401 Unauthorized'}, 401


api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')











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


@app.route('/books/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def bookById(id):
    book = Book.query.filter_by(id=id).first()

    if request.method == 'GET':
        if book:
            book_dict = book.to_dict() 

            response = make_response(
                jsonify(book_dict),
                    200
            )
        else:
            response = make_response(
                {"error": "Book not fount"},
                404
            )

        return response
    
    elif request.method == 'DELETE':
        book = Book.query.filter(Book.id == id).first()

        if not book:
            response = make_response(
                {"error": "Book not found"},
                404
            )
            return response
        
        db.session.delete(book)
        db.session.commit()
        return make_response({'success':"DELETED"}, 200)
    
    elif request.method == 'PATCH':
        book = Book.query.filter(Book.id == id).first()

        if not book:
            response = make_response(
                {"error": "Book not fount"},
                404
            )
            return response
        
        for attr in request.get_json():
            setattr(book, attr, request.get_json()[attr])

        db.session.add(book)
        db.session.commit()

        return make_response(
            book.to_dict(),
            200
        )




@app.route('/quotes', methods=['GET', 'POST'])
def quote():
    quotes = Quote.query.all()
    if request.method == 'GET':
        quotes_dict = [quote.to_dict() for quote in quotes]

        response = make_response(
            jsonify(quotes_dict),
            200
        )

        return response
    

    elif request.method == 'POST':

        try:
            new_quote = Quote(
                quote = request.get_json()['quote'],
                book_id = request.get_json()['book_id']
            )
            db.session.add(new_quote)
            db.session.commit()

            response = make_response(
                jsonify(new_quote.to_dict()),
                201
            )

        except ValueError:

            response = make_response(
                {"error": "validation errors"},
                400
            )
    return response


# @app.route('/reviews/<int:id>', methods=['GET', 'POST'])
# def review(id):
#     review = Review.query.filter_by(book_id=id).first()
#     if request.method == 'GET':
#         if review:
#             review_dict = review.to_dict() 

#             response = make_response(
#                 jsonify(review_dict),
#                     200
#             )
#         else:
#             response = make_response(
#                 {"error": "Book not fount"},
#                 404
#             )

#         return response
    

#     elif request.method == 'POST':

#         try:
#             new_review = Review(
#                 review = request.get_json()['review'],
#                 user_id = request.get_json()['user_id'],
#                 book_id = request.get_json()['book_id']
#             )
#             db.session.add(new_review)
#             db.session.commit()

#             response = make_response(
#                 jsonify(new_review.to_dict()),
#                 201
#             )

#         except ValueError:

#             response = make_response(
#                 {"error": "validation errors"},
#                 400
#             )
#     return response

@app.route('/reviews', methods=['GET', 'POST'])
def review():
    reviews = Review.query.all()
    if request.method == 'GET':
        reviews_dict = [review.to_dict() for review in reviews]

        response = make_response(
            jsonify(reviews_dict),
            200
        )

        return response
    

    elif request.method == 'POST':

        try:
            new_review = Review(
                review = request.get_json()['review'],
                # user_id = request.get_json()['user_id'],
                book_id = request.get_json()['book_id']
            )
            db.session.add(new_review)
            db.session.commit()

            response = make_response(
                jsonify(new_review.to_dict()),
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
