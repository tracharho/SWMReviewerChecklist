from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import app.get_data_from_csvs

app = Flask(__name__, static_folder='static')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login' #requires user to be logged in to view certain pages


get_data_from_csvs.categorizeCsvs()

from app import routes, models, makeletter, get_data_from_csvs