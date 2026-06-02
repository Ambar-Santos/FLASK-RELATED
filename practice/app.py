#Initialization 
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'watapatapitusberry'

bootstrap = Bootstrap(app)

#Class for WTForms package 
class NameForm(FlaskForm):
   name = StringField('What is your name', validators=[DataRequired()])
   submit = SubmitField('Submit')


#Routes
   
@app.route('/')
def index():
    form = NameForm()
    return render_template('index.html', form=form)

@app.route('/user/<user>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
   return render_template('500.html'), 500
 


if __name__ == '__main__':
  app.run(debug=True)