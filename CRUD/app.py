from flask import Flask 


app = Flask(__name__)

app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request()
def create_table():
    db.create_all()