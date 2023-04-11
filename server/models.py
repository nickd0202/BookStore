from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, bcrypt
# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-book_review', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    book_review = db.relationship('Review', backref='user')
    books = association_proxy('book_review', 'book')

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'<User {self.username}>'
    

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    serialize_rules = ('-book_review', '-book_quote', '-created_at', '-updated_at', '-Review')

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