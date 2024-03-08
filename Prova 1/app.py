# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from tinydb import TinyDB, Query, where

app = Flask(__name__)

db = TinyDB("caminhos.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novo", methods=["GET", "POST"])
def novo(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        db.insert({"nome": nome})
    posts = db.all()
    return render_template("novo.html", nome=nome, posts=posts)

@app.route("/pegar_caminho/<int:id>")    
def pegar_caminho(id):
    return jsonify(db.get(doc_id=id))

@app.route("/listas_caminhos")    
def listas_caminhos():
    return jsonify(db.all())

@app.route("/atualizar/<int:id>, <string:texto>")    
def atulizar(id, texto):
    return jsonify(db.update(doc_id=id, cond="nome",fields=texto))

@app.route("/deletar/<int:id>")    
def deletar(id):
    qr = Query()
    return db.remove(qr.id == id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)