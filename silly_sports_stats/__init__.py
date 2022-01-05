from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from silly_sports_stats.secret_data import secret_key
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Temp secret key
app.config["SECRET_KEY"] = secret_key
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from silly_sports_stats import routes
