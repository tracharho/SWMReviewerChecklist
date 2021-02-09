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
    recipient = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    checklists = db.relationship('Checklist', backref='project_name', lazy='dynamic')

    def __repr__(self):
        return '<project {} {}>'.format(self.dsc_number, self.name)

class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    rows = db.relationship('ModifiedRow', backref='checklist_name', lazy='dynamic')

class ModifiedRow(db.Model):
    row_number = db.Column(db.String, primary_key=True)
    row_id = db.Column(db.Integer, db.ForeignKey('checklist.id'))
    category = db.Column(db.String(50))
    subcategory = db.Column(db.String(50))
    checked = db.Column(db.Boolean(), default = False, nullable=False)
    Criteria = db.Column(db.String(240), unique=True)
    Comment = db.Column(db.String(240), unique=True)
    Ceference = db.Column(db.String(70))

#The table containing rows of the original checklist 
#The intent is to have the checklist load these rows in by default, but check
#if the project in use has a checked checkbox and/or entry text. If yes, then
#load the user's specific row in that place. 
class OriginalRow(db.Model):
    rownum = db.Column(db.String, primary_key=True)
    category = db.Column(db.String(50))
    subcategory = db.Column(db.String(50))
    checked = db.Column(db.Boolean(), default = False, nullable=False)
    Criteria = db.Column(db.String(240), unique=True)
    Comment = db.Column(db.String(240), unique=True)
    Reference = db.Column(db.String(70))
    


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#$ flask db migrate -m "migrate message"
#$ flask db upgrade