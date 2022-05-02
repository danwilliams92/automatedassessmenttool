from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from openpyxl import load_workbook

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c9ddf3c61037ad426abd6262587fd8757ba49e6f01772beb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')

db = SQLAlchemy(app)
from mainApp import routes