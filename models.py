from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModeloTarefa(db.Model):
    __tablename__ = "tarefas"
 
    id = db.Column(db.Integer, primary_key=True, unique = True)
    # id_tarefa = db.Column(db.Integer(), unique = True)
    titulo = db.Column(db.String())
    status = db.Column(db.Integer())
 
    def __init__(self, titulo, status):
        # self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.status = status
 
    def __repr__(self):
        return "{'titulo': '"+str(self.titulo)+"', 'id_tarefa': '"+str(self.id)+"', 'status': '"+str(self.status)+"'}"