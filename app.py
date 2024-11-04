from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/planos")
def planos():
    return render_template("planos.html")

@app.route("/dominio")
def compras():
    return render_template("compras.html")
app.run(debug=True)
