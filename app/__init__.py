from flask import Flask, session, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flaskwebgui import FlaskUI

app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
ui = FlaskUI(app, width=1200, height=1200)


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login' #requires user to be logged in to view certain pages



from app import routes, models, makeletter
ui.run()
