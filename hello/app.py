from flask import Flask, render_template, request



#Turn this app into a webapp and give me a variable called app
#to reference it
app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")



@app.route("/greet")
def greet():
  name = request.args.get("name", "world")
  return render_template("greet.html", name=name)