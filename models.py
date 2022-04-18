# pylint: skip-file
"""Models for the database"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Joes(db.Model, UserMixin):
    """This will create the user object
    portion of our database and hold the users.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return "Username %r" % self.username


class Entry(db.Model):
    """This will create our entry object portion,
    which will be stored in our database.
    """

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(1500), nullable=False)
    timestamp = db.Column(db.String(100))

    def __repr__(self):
        return "User: %s posted: %s, and titled it ' %s ', at " "the time of %s" % (
            self.user,
            self.content,
            self.title,
            self.timestamp,
        )


class Task(db.Model):
    """This will create our entry object portion,
    which will be stored in our database.
    """

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(1500), nullable=False)

    def __repr__(self):
        return "User: %s posted: %s, and titled it ' %s" % (
            self.user,
            self.content,
            self.title,
        )
