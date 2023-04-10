from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-book_review', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    book_review = db.relationship('Review', backref='user')
    books = association_proxy('book_review', 'book')

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    serialize_rules = ('-book_review', '-book_quote', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    publishDate = db.Column(db.String)
    genre = db.Column(db.String)
    link = db.Column(db.String)
    summary = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())


    book_review = db.relationship('Review', backref='book')
    users = association_proxy('book_review', 'user')

    book_quote = db.relationship('Quote', backref='book')

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    serialize_rules = ('-user.book_review', '-book.book_review', '-book_review', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'

    serialize_rules = ('-book.book_quote', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))