from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from todo import config
from secrets import token_hex
import os


root_path = os.path.curdir


app = Flask(__name__)
db = SQLAlchemy(app)
# app.config.from_json(config.conf)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"] = token_hex(20)


from todo import routes
