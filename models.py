from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
 
# class EmployeeModel(db.Model):
#     __tablename__ = "employee"
 
#     id = db.Column(db.Integer, primary_key=True)
#     employee_id = db.Column(db.Integer(),unique = True)
#     name = db.Column(db.String())
#     age = db.Column(db.Integer())
#     position = db.Column(db.String(80))
 
#     def __init__(self, employee_id,name,age,position):
#         self.employee_id = employee_id
#         self.name = name
#         self.age = age
#         self.position = position
 
#     def __repr__(self):
        
#         # return f"{self.name}:{self.employee_id}"
#         ret = {'id':self.employee_id,'name':self.name,'age':self.age,'position':self.position}
#         return json.dumps(ret)
            

class TaskModel(db.Model):
    __tablename__ = "task"
 
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer(),unique = True)
    title = db.Column(db.String())
    status = db.Column(db.Integer())
 
    def __init__(self, task_id,title, status):
        self.task_id = task_id
        self.title = title
        self.status = status
 
    def __repr__(self):
        # ret = {'id':self.task_id,'title':self.title,'status':self.status}
        # return json.loads(ret)
        return f"{self.title}:{self.task_id}:{self.status}"
