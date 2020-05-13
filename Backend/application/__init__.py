from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_replicated import FlaskReplicated

application = Flask(__name__, template_folder='../templates')


application.config.from_object('config')

db = SQLAlchemy(application)

FlaskReplicated(application)
