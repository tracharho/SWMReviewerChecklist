from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import cast

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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(140), nullable=False, unique=True)
    dsc_number = db.Column(db.String(20), nullable=False)
    recipient = db.Column(db.String(30), nullable=False)
    checklist = db.column_property("Checklist-"+db.cast(id,db.String))
    checklist_is_original = db.Column(db.Boolean,default=True, nullable=True)
    rows = db.relationship('ModifiedRow', backref='saved_comment', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return '<name {} dsc_number {} recipient {} checklist {}>'.format(self.dsc_number, self.name, self.recipient, self.checklist)

class ModifiedRow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.String)
    parent_project_id  = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'))
    Comment = db.Column(db.String(240))
    
#The table containing rows of the original checklist 
#The intent is to have the checklist load these rows in by default, but check
#if the project in use has a checked checkbox and/or entry text. If yes, then
#load the user's specific row in that place. 
class OriginalRow(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.String, unique=True)
    category = db.Column(db.String(50))
    subcategory = db.Column(db.String(50))
    checked = db.Column(db.Boolean(), default = False, nullable=False)
    Criteria = db.Column(db.String(240))
    Comment = db.Column(db.String(240))
    Reference = db.Column(db.String(70))
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#$ flask db migrate -m "migrate message"
#$ flask db upgrade
