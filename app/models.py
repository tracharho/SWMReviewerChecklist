from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    projects = db.relationship('Project', backref='author', lazy='dynamic')

    #this method tells Python how to print objects of this class
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    dsc_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    checklists = db.relationship('Checklist', backref='project_name', lazy='dynamic')

    def __repr__(self):
        return '<project {} {}>'.format(self.dsc_number, self.name)

class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#Models can only be edited through flask sql alchemy!
#$ flask db migrate -m "migrate message"
#$ flask db upgradte