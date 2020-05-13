from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.routing import AutoRouteSQLAlchemy

application = Flask(__name__, template_folder='../templates')


application.config.from_object('config')
db = AutoRouteSQLAlchemy(application)
