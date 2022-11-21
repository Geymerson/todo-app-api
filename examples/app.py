# The source code for this tutorial is available at https://www.askpython.com/python-modules/flask/flask-crud-application

from flask import Flask, render_template, request, redirect
from models import db, EmployeeModel

app = Flask(__name__, template_folder='templates')

# Configuracoes da base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


# Definicao da rota de escrita de dados
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')

# Definicao da rota de consulta de dados
@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    print(employees)
    return render_template('datalist.html',employees = employees)


#Definicao da rota de consulta de dados de um unico empregado
@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"


# Definicao da rota de atualizacao de dados de um unico empregado
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
 
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
 
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('update.html', employee = employee)


# Definicao da rota de remocao de dados de um unico empregado
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')

app.run(host='localhost', port=5000)