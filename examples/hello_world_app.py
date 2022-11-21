from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World'

# Configurar nome do site porta onde as requisicoes serao recebidas
app.run(host='localhost', port=5000)