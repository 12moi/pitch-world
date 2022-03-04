

import email
from enum import unique
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from . import db,login_manager
from datetime import datetime

class User(UserMixin, db.model):
    _tablename_='users'
    id=db.column(db.string(255),unique=True,nullabl=False)
    username=db.column(db.string(255),unique=True,nullabl=False)
    email=db.column(db.string(255),unique=True,nullabl=False)
    secure_password=db.column(db.string(255),unique=True,nullabl=False)
    bio=db.column(db.string(255))
    profle_pic_path=db.column(db.string())
    pitches=db.relationship('Pitch', backref='user', lazy='dynamic')
    comment=db.relationship('Comment', backref='user', lazy='dynamic')
    upvote=db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote=db.relationship('Downvote', backref='user', lazy='dynamic')

    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'