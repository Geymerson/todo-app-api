from routes import app

if __name__ == '__main__':
    print('Iniciando o servidor')
    app.run(host='localhost', port=5000)