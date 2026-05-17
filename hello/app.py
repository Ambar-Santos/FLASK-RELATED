from flask import Flask, render_template, request



#Turn this app into a webapp and give me a variable called app
#to reference it
app = Flask(__name__)


@app.route("/")
def index():

    name = request.args.get("name", "world") #world being default value
    return render_template("index.html", name=name)
                           #positional

