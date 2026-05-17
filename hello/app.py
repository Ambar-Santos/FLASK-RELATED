from flask import Flask
render_template



#Turn this app into a webapp and give me a variable called app
#to reference it
app = Flask(__name__)


@app.route("/")
def index():
  
    return render_template("index_html")