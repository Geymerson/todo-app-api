# todo-app-project


Instalando os módulos
> pip install -r requirements.txt

Executando a aplicação
> python main.py

## Rotas

Rota para consulta de todas as tarefas (considerando porta 5000)

> http://localhost:5000/tarefas

Rota para cadastrar uma tarefa

> http://localhost:5000/tarefas/cadastrar

Rota para consulta de todas as tarefas ativas

> http://localhost:5000/tarefas/ativas

Rota para consulta de todas as tarefas finalizadas

> http://localhost:5000/tarefas/finalizadas

Rota para consultar uma tarefa com id <int>

> http://localhost:5000/tarefas/<int:id>

Rota para atualizar uma tarefa com id <int>

> http://localhost:5000/tarefas/<int:id>/atualizar

Rota para deletar uma tarefa com id <int>

> http://localhost:5000/tarefas/<int:id>/deletar

Rota para deletar de todas as tarefas

> http://localhost:5000/tarefas/deletar
