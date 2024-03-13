from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "E AI MUNDO!"

@app.route("/about")
def about():
    return "Pagina sobre!"

if __name__ == "__main__": # Desevolvimento local (na propria máquina)
    app.run(debug=True)