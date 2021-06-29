from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Initialization
app = Flask(__name__)

# orm config
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://lugman:password@localhost/movies"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DB config
db = SQLAlchemy(app)
ma = Marshmallow(app)


from app.routes import movie
from app.routes import company
