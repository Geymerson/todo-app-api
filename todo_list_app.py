from flask import Flask, render_template, request, redirect, jsonify, json
from models import db, TaskModel

app = Flask(__name__, template_folder='todo_templates')

# Configuracoes da base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# Definicao da rota de consulta de dados
@app.route('/data')
def RetrieveDataList():
    tasks = TaskModel.query.all()
    print(tasks[0])
    # print(type(tasks))
    # print(tasks)
    # return tasks
    return 'Ok'
    # return tasks
    # return render_template('datalist.html',tasks = tasks)

# Definicao da rota de escrita de dados
@app.route('/data/create' , methods = ['POST'])
def create():
    task_id = request.form['task_id']
    title = request.form['title']
    status = request.form['status']
    task = TaskModel(task_id=task_id, title=title, status=status)
    db.session.add(task)
    db.session.commit()
    return 'Ok'

# Definicao da rota de consulta de dados de tarefas ativas
@app.route('/data/active')
def RetrieveActiveDataList():
    tasks = TaskModel.query.filter_by(status=False)
    return render_template('datalist.html',tasks = tasks)

# Definicao da rota de consulta de dados de tarefas finalizadas
@app.route('/data/complete')
def RetrieveCompleteDataList():
    tasks = TaskModel.query.filter_by(status=True)
    return render_template('datalist.html',tasks = tasks)


#Definicao da rota de consulta de dados de uma unica tarefa
@app.route('/data/<int:id>')
def RetrieveSingleTask(id):
    task = TaskModel.query.filter_by(task_id=id).first()
    if task:
        return render_template('data.html', task = task)
    return f"Task with id ={id} Doenst exist"

# Definicao da rota de atualizacao de dados de um aunica tarefa
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    task = TaskModel.query.filter_by(task_id=id).first()
    if request.method == 'POST':
        if task:
            db.session.delete(task)
            db.session.commit()
 
            title = request.form['title']
            status = request.form['status']
            task = TaskModel(task_id=id, name=title, status=status)
 
            db.session.add(task)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Task with id = {id} Does nit exist"
 
    return render_template('update.html', task = task)


# Definicao da rota de remocao de dados de uma unica tarefa
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    task = TaskModel.query.filter_by(task_id=id).first()
    if request.method == 'POST':
        if task:
            db.session.delete(task)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')

# Definicao da rota de remocao de dados de uma unica tarefa
@app.route('/data/delete', methods=['DELETE'])
def deleteAll():
    db.session.query(TaskModel).delete()
    db.session.commit()
    return redirect('/data')

app.run(host='localhost', port=5000)