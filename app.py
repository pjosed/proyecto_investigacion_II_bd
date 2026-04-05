from flask import Flask, render_template, request, redirect
from functions import *
# Este archivo es el servidor de la aplicación web, se encarga de recibir las solicitudes del usuario y llamar a las funciones correspondientes para realizar las operaciones solicitadas

app = Flask(__name__)

# -------------------------
# MENU
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")

# -------------------------
# OPCION 1 - CRUD AUTOR / LIBRO / EDICION / COPIA
# -------------------------
@app.route("/crud")
def crud():
    return render_template("crud.html")

# -------------------------
# AUTOR
# -------------------------
@app.route("/autor")
def autor():
    autores = obtener_autores()
    return render_template("autor.html", autores=autores)

@app.route("/autor/insertar", methods=["POST"])
def insertar_autor_route():
    insertar_autor(request.form["nombre"])
    return redirect("/autor")

@app.route("/autor/actualizar", methods=["POST"])
def actualizar_autor_route():
    actualizar_autor(
        request.form["nombre"],
        request.form["nuevo"]
    )
    return redirect("/autor")

@app.route("/autor/borrar", methods=["POST"])
def borrar_autor_route():
    borrar_autor(request.form["nombre"])
    return redirect("/autor")

@app.route("/libro")
def libro():
    libros = obtener_libros()
    return render_template("libro.html", libros=libros)

@app.route("/libro/insertar", methods=["POST"])
def insertar_libro_route():
    insertar_libro(request.form["titulo"])
    return redirect("/libro")

@app.route("/libro/actualizar", methods=["POST"])
def actualizar_libro_route():
    actualizar_libro(
        request.form["titulo"],
        request.form["nuevo"]
    )
    return redirect("/libro")

@app.route("/libro/borrar", methods=["POST"])
def borrar_libro_route():
    borrar_libro(request.form["titulo"])
    return redirect("/libro")

@app.route("/edicion")
def edicion():
    libros = obtener_libros()
    return render_template("edicion.html", libros=libros)

@app.route("/edicion/insertar", methods=["POST"])
def insertar_edicion_route():
    insertar_edicion(
        request.form["titulo"],
        request.form["isbn"],
        request.form["anio"],
        request.form["idioma"]
    )
    return redirect("/edicion")

@app.route("/copia")
def copia():
    libros = obtener_libros()
    return render_template("copia.html", libros=libros)

@app.route("/copia/insertar", methods=["POST"])
def insertar_copia_route():
    insertar_copia(
        request.form["titulo"],
        request.form["isbn"],
        int(request.form["numero"])
    )
    return redirect("/copia")





# -------------------------
# OPCION 2 - USUARIOS
# -------------------------
@app.route("/usuarios")
def usuarios():
    usuarios = obtener_usuarios()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/insertar", methods=["POST"])
def insertar_usuario_route():
    insertar_usuario(request.form["rut"], request.form["nombre"])
    return redirect("/usuarios")

@app.route("/usuarios/actualizar", methods=["POST"])
def actualizar_usuario_route():
    actualizar_usuario  (request.form["rut"], request.form["nuevo"])
    return redirect("/usuarios")

@app.route("/usuarios/borrar", methods=["POST"])
def borrar_usuario_route():
    borrar_usuario(request.form["rut"])
    return redirect("/usuarios")








# -------------------------
# OPCION 3 - PRESTAMOS
# -------------------------
@app.route("/prestamos")
def prestamos():
    return "CRUD PRESTAMO (pendiente)"

# -------------------------
# OPCION 4 - CONSULTAS
# -------------------------
@app.route("/consultas")
def consultas():
    return render_template("consultas.html")
# -------------------------
# CONSULTA#1
# -------------------------
@app.route("/primer-cnslt")
def consulta1():
    copias = obtener_copias_libros()
    return render_template("consulta#1.html", copias=copias)
# -------------------------
# CONSULTA#2
# -------------------------
@app.route("/segunda-cnslt",methods=["GET", "POST"])
def consulta2():
    if request.method == "POST":
        rut = request.form["rut"]
        prestamos = obtener_prestamos_lib(rut)
        return render_template("consulta#2.html", prestamos=prestamos)
    return render_template("consulta#2.html")
# -------------------------
# EJECUTAR
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)