# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, ModeloTarefa

app = Flask(__name__)

# Configuracoes da base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)

@app.before_first_request
def criar_banco_de_dados():
    db.create_all()

# Definicao da rota da página inicial
@app.route('/')
def home():
    return 'Olá, mundo! O servidor está online!'

# Definicao da rota de consulta de dados
@app.route('/tarefas')
def carregar_tarefas():
    tarefas = ModeloTarefa.query.all()
    return jsonify(str(tarefas))

# Definicao da rota de escrita de dados
@app.route('/tarefas/cadastrar' , methods = ['POST'])
def cadastrar_tarefa():
    titulo = request.form['titulo']
    status = request.form['status']
    if(status == '0' or status == '1'):
        tarefa = ModeloTarefa(titulo=titulo, status=status)
        db.session.add(tarefa)
        db.session.commit()
        return jsonify({'resposta': 'sucesso'})
    return jsonify({'resposta': 'falha', 'erro': 'código de status deve ser 1 ou 0'})

# Definicao da rota de consulta de dados de tarefas ativas
@app.route('/tarefas/ativas', methods = ['GET'])
def carregar_tarefas_ativas():
    tarefas = ModeloTarefa.query.filter_by(status=0).all()
    return jsonify(str(tarefas))

# Definicao da rota de consulta de dados de tarefas finalizadas
@app.route('/tarefas/finalizadas')
def carregar_tarefas_finalizadas():
    tarefas = ModeloTarefa.query.filter_by(status=1).all()
    return jsonify(str(tarefas))

# Definicao da rota de consulta de dados de uma unica tarefa
@app.route('/tarefas/<int:id>')
def buscar_tarefa(id):
    tarefa = ModeloTarefa.query.filter_by(id=id).first()
    if tarefa:
        return jsonify(str(tarefa))
    return jsonify({'resposta': 'não encontrada'})

# Definicao da rota de atualizacao de dados de uma unica tarefa
@app.route('/tarefas/<int:id>/atualizar', methods = ['POST', 'PUT'])
def atualizar_tarefa(id):
    tarefa = ModeloTarefa.query.filter_by(id=id).first()
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()

        titulo = request.form['titulo']
        status = request.form['status']
        tarefa = ModeloTarefa(titulo=titulo, status=status)

        db.session.add(tarefa)
        db.session.commit()
        return jsonify({'resposta': 'sucesso'})
    return jsonify({'resposta': 'não encontrada'})

# Definicao da rota de remocao de dados de uma unica tarefa
@app.route('/tarefas/<int:id>/deletar', methods = ['POST', 'DELETE'])
def deletar_tarefa(id):
    tarefa = ModeloTarefa.query.filter_by(id=id).first()
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'resposta': 'sucesso'})
    return jsonify({'resposta': 'não encontrada'})

# Definicao da rota de remocao de dados de todas as tarefas
@app.route('/tarefas/deletar', methods=['POST', 'DELETE'])
def deletar_todas():
    db.session.query(ModeloTarefa).delete()
    db.session.commit()
    return jsonify({'resposta': 'sucesso'})