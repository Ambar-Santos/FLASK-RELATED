from flask import Flask, render_template, request, session
from flask_session from Session

app = Flask(__name__)

#configure for session 

app.config["SESSION_PERMANENT"] = False
app.congig["SESSION_TYPE"] = "fylesystem"
Session(app)

