#Setting up 

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'a_very_secret_key'
db = SQLAlchemy(app)

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
    if form.valdate_on_submit():
        item = Item(name=form.name.data, description=form.description.data)
        db.session.add(item)
        db.session.commit()
        flash('Item created succesfully!')
        return redirect(url_for('index'))
    return render_template('create.html', form=form)
      
# Edit existing item (update)
@app.rout('/edit/', method=['GET', 'POST'])
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

# Delete item 
@app.route('/delete', methods=['POST'])
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!')
    return redirect(url_for('index'))