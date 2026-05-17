from flask import Flask, render_template, request # pyright: ignore[reportMissingImports]



#Turn this app into a webapp and give me a variable called app
#to reference it
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
     if request.method == "POST":
         name = request.form.get("name")
         return render_template("greet.html", name=name)
     else: 
         return render_template("index.html")



