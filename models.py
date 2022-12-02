from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModeloTarefa(db.Model):
    __tablename__ = "tarefas"
 
    id = db.Column(db.Integer, primary_key=True, unique = True)
    titulo = db.Column(db.String())
    status = db.Column(db.Integer())
 
    def __init__(self, titulo, status):
        self.titulo = titulo
        self.status = status
 
    def __repr__(self):
        return "{'titulo': '"+str(self.titulo)+"', 'id_tarefa': '"+str(self.id)+"', 'status': '"+str(self.status)+"'}"