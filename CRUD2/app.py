#Setting up 

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'a_very_secret_key'
db = SQLAlchemy(app)
