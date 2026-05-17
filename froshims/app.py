from flask import Flask, render_template, request  # type: ignore



app = Flask(__name__)


@app.route("/")
def index():
  return "hello world"