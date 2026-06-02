from flask import Flask, request, render_template, redirect
from models import db, EmployeeModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#CREATE
@app.route('/data/create', methods=['GET', 'POST'])
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
  
#RETRIEVE
#retrieve all employees
@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html', employees=employees) #emplayees=listofemployees

#retrieve specific employee
@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee=employee) #employeeforhtml=variablepython
    return f"Employee with id={id} Does not exist"

#Update 
@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()

            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position=position)

            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id{id} does not exist" 
    return render_template('update.html', employee=employee)

#Delete
@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id): 
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee: 
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        abort(404)
    return render_template('delete.html')

#run server
if __name__ == '__main__':
  app.run(debug=True)