from flask import Flask, request, render_template, flask_sqalchemy


app = Flask(__name__)

app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request()
def create_table():
    db.create_all() 


@app.route('data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')