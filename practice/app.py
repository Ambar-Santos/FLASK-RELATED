#Initialization 
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<user>')
def user(user):
    return render_template('user.html', user=user)


if __name__ == '__main__':
  app.run(debug=True)