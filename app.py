from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    arr =["Luis", "Paco","Rosita", "Martin", "Elsa"]
    autor = "Evelyn Fernanda Caldera Gallegos"
    return render_template("index.html", nombre = autor, amigos = arr)
    
@app.route("/1")
def pp1():
    arr =["Daniela", "Leonardo", "Loretto","Luis"]
    autor = "Evelyn Fernanda Caldera Gallegos"
    return render_template("pp1.html", nombre = autor, amigos = arr)

@app.route("/2")
def pp2():
    arr =["1", "2", "3","4"]
    autor = "Evelyn Fernanda Caldera Gallegos"
    return render_template("pp2.html", nombre = autor, amigos = arr)

@app.route("/3")
def pp3():
    arr =["azul", "rojo", "verde","morado"]
    autor = "Evelyn Fernanda Caldera Gallegos"
    return render_template("pp3.html", nombre = autor, amigos = arr)

if __name__ == "__main__":
    app.run(debug=True)