from flask import Flask, render_template, request, redirect
from db import db
from functions import *

app = Flask(__name__)

# -------------------------
# MENU PRINCIPAL
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -------------------------
# CRUD AUTOR
# -------------------------
@app.route("/crud")
def crud():
    return render_template("crud.html")

autor_col = db["autor"]

@app.route("/autor")
def autor():
    autores = list(autor_col.find())
    return render_template("autor.html", autores=autores)

@app.route("/autor/insertar", methods=["POST"])
def insertar_autor():
    nombre = request.form["nombre"]
    autor_col.insert_one({"nombre": nombre})
    return redirect("/autor")

@app.route("/autor/actualizar", methods=["POST"])
def actualizar_autor():
    nombre = request.form["nombre"]
    nuevo = request.form["nuevo"]

    autor_col.update_one(
        {"nombre": nombre},
        {"$set": {"nombre": nuevo}}
    )

    return redirect("/autor")

@app.route("/autor/borrar", methods=["POST"])
def borrar_autor():
    nombre = request.form["nombre"]
    autor_col.delete_one({"nombre": nombre})
    return redirect("/autor")


libro_col = db["libro"]

# -------------------------
# CRUD LIBRO
# -------------------------

@app.route("/libro")
def libro():
    libros = list(libro_col.find())
    return render_template("libro.html", libros=libros)

@app.route("/libro/insertar", methods=["POST"])
def insertar_libro():
    titulo = request.form["titulo"]
    libro_col.insert_one({"titulo": titulo, "ediciones": []})
    return redirect("/libro")

@app.route("/libro/actualizar", methods=["POST"])
def actualizar_libro():
    titulo = request.form["titulo"]
    nuevo = request.form["nuevo"]

    libro_col.update_one(
        {"titulo": titulo},
        {"$set": {"titulo": nuevo}}
    )

    return redirect("/libro")

@app.route("/libro/borrar", methods=["POST"])
def borrar_libro():
    titulo = request.form["titulo"]
    libro_col.delete_one({"titulo": titulo})
    return redirect("/libro")



# -------------------------
# CRUD EDICION
# -------------------------

@app.route("/edicion")
def edicion():
    libros = list(libro_col.find())
    return render_template("edicion.html", libros=libros)

@app.route("/edicion/insertar", methods=["POST"])
def insertar_edicion():
    titulo = request.form["titulo"]
    isbn = request.form["isbn"]
    año = request.form["anio"]
    idioma = request.form["idioma"]

    libro_col.update_one(
        {"titulo": titulo},
        {
            "$push": {
                "ediciones": {
                    "ISBN": isbn,
                    "año": año,
                    "idioma": idioma,
                    "copias": []
                }
            }
        }
    )

    return redirect("/edicion")

# -------------------------
# CRUD COPIA
# -------------------------

@app.route("/copia")
def copia():
    libros = list(libro_col.find())
    return render_template("copia.html", libros=libros)

@app.route("/copia/insertar", methods=["POST"])
def insertar_copia():
    titulo = request.form["titulo"]
    isbn = request.form["isbn"]
    numero = int(request.form["numero"])

    libro_col.update_one(
        {
            "titulo": titulo,
            "ediciones.ISBN": isbn
        },
        {
            "$push": {
                "ediciones.$.copias": {
                    "numero": numero
                }
            }
        }
    )

    return redirect("/copia")

# -------------------------
# ESTRUCTURA RESTANTE
# -------------------------

# -------------------------
# CRUD usuario
# -------------------------
@app.route("/usuarios")
def usuarios():
    return "CRUD USUARIOS (pendiente)"


# -------------------------
# CRUD Prestamo
# -------------------------
@app.route("/prestamos")
def prestamos():
    return "CRUD PRESTAMOS (pendiente)"

# -------------------------
# CRUD CONSULTAS
# -------------------------
@app.route("/consultas")
def consultas():
    return "CONSULTAS (pendiente)"


if __name__ == "__main__":
    app.run(debug=True)