from flask import Flask, render_template, request  # type: ignore

#canonical global variable 
SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee",
]


app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
  if not request.form.get("name") or request.form.get("sport"):
    return render_template("failure.html")
  else:
    return render_template("success.html")