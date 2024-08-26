from flask import Flask, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

todos = []

class Base(DeclarativeBase):
  pass

db = SQLAlchemy()
app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# from app.controllers import default





