# puppycompanyblog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

###########################
### DATABASE SETUP ########
###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#########################
# LOGIN CONFIGS #########
#########################
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

######################################
########### IMPORT VIEWS #############
######################################
from home.views import home
from error_pages.handlers import error_pages
from users.views import users
from blogs.views import blogs
from projects.views import projects
app.register_blueprint(home)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blogs)
app.register_blueprint(projects)