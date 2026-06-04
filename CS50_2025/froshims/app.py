from flask import Flask, render_template, request  # type: ignore

#canonical global variable 
SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee",
]

#store in memory 


REGISTRANTS = {

}





app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if sport not in SPORTS and not name:
      return render_template("error.html", message="No name and no sport introduced")
    
    if not name:
       return render_template("error.html", message="Missing Name")
    
    if not sport:
       return render_template("error.html", message="Missing Sport")
    
    if sport not in SPORTS:
       return render_template("error.html", message="Invalid Sport")
    
    REGISTRANTS[name] = sport

    return render_template("success.html")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)