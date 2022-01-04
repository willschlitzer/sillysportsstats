from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from silly_sports_stats.secret_data import secret_key




app = Flask(__name__)

# Temp secret key
app.config["SECRET_KEY"] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)

from silly_sports_stats import routes