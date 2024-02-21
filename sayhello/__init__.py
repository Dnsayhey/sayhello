from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

app = Flask("sayhello")
app.config.from_pyfile("settings.py")

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)

from sayhello import commands, errors, views
