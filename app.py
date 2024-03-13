from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD -> CREATE - READ - UPDATE - DELETE

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control,title=data['title'],description=data.get("description",""))
    task_id_control+=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'Message':"Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    #task_list = []
    #for task in tasks:
    #    task_list.append(task.to_dict())
    
    output = {
        "tasks": task_list,
        "total_tasks":len(task_list)
    }

    #output = {
    #    "tasks":[
    #        {
    #        "id":0,
    #        "title":"string",
    #        "description":"string",
    #        "completed":true
    #        }
    #    ],
    #    "total_tasks":0
    #}
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({'Message': "Não foi possivel encontrar a task"}),404

# Exemplo de rota
#@app.route('/user/<username>') 
#def show_user(username):
#    print(username)
#    print(type(username))
#    return username

@app.route('/tasks/<int:id>',methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({'Message': "Não foi possivel encontrar a task"}),404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message":"Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>',methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({'Message': "Não foi possivel encontrar a task"}),404

    tasks.remove(task)
    return jsonify({'Message': "Task deletada com sucesso"})
    

if __name__ == "__main__": # Desevolvimento local (na propria máquina)
    app.run(debug=True)