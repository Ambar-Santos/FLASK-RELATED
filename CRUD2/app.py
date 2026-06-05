#Setting up 
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 
from forms import ItemForm
import os
from models import db,Item

basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'a_very_secret_key'
db.init_app(app)

#display all of the items
#handling crud operations

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

# Create new item 
@app.route('/create', methods=['GET','POST'])
def create():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, description=form.description.data)
        db.session.add(item)
        db.session.commit()
        flash('Item created succesfully!')
        return redirect(url_for('index'))
    return render_template('create.html', form=form)
      
# Edit existing item (update)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Item.query.get_or_404(id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        db.session.commit()
        flash('Item succesfully updated!')
        return redirect(url_for('index'))
    return render_template('update.html', form=form, item=item)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_confirmation(id):
    item = Item.query.get_or_404(id)
    return render_template('delete.html', item=item)





# Delete item 
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
  with app.app_context():
      db.create_all()
  app.run(debug=True, port=8001)