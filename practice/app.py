#Initialization 
from flask import Flask, redirect, render_template, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy 

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

#DATABASE CONFIGURATION  
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'watapatapitusberry'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

#Class for WTForms package 
class NameForm(FlaskForm):
   name = StringField('What is your name', validators=[DataRequired()])
   submit = SubmitField('Submit')


#Models
class Role(db.model):
   __tablename__ = 'roles'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), unique=True)

   def __repr__(self):
      return '<Role%r>' % self.name 
   
class User(db.model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), unique=True, index=True)

   def __repr__(self):
      return '<User %r>' % self.username









#Routes
@app.route('/', methods=['GET', 'POST']) #get is not secure for forms, so post it is
def index():
    form = NameForm()
    if form.validate_on_submit():
      old_name = session.get('name')
      if old_name is not None and old_name != form.name.data:
         flash(f'Looks like you have changed your name to {form.name.data}, interesting!')
         session['name'] = form.name.data
         return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
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