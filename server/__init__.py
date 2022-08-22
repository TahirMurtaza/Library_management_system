import os
from sys import prefix
from flask import Flask
from .extensions import db
from .views.members_view import membersview 
from .views.books_view import booksview 
from flask_migrate import Migrate


def create_app():
   
    app = Flask(__name__)
    # Since Flask login uses sessions for authentication, create a secret key on your application.
    SECRET_KEY = os.urandom(32)
    #SqlAlchemy Database Configuration With db sqlite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)
    # Build the database:
    # This will create the database file using SQLAlchemy
    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db, compare_type=True)

    app.register_blueprint(membersview,url_prefix='/api/members')
    app.register_blueprint(booksview,url_prefix='/api/books')
    
    return app

