from flask import Flask, render_template, request



#Turn this app into a webapp and give me a variable called app
#to reference it
app = Flask(__name__)


@app.route("/")
def index():


    if "name" in request.args: 
        name = request.args["name"]
    else:
        name = "world"
    return render_template("index.html", name=name)
                           #positional

