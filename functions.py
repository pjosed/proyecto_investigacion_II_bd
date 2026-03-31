from db import db


#Este archivo hace operaciones con la base de datos y es llamado por el app.py para realizar las operaciones solicitadas por el usuario

autor_col = db["autor"]
libro_col = db["libro"]
usuario_col = db["usuario"]
# ---------------- AUTOR ----------------

def obtener_autores():
    return list(autor_col.find())

def insertar_autor(nombre):
    autor_col.insert_one({"nombre": nombre})

def actualizar_autor(nombre, nuevo):
    autor_col.update_one(
        {"nombre": nombre},
        {"$set": {"nombre": nuevo}}
    )

def borrar_autor(nombre):
    autor_col.delete_one({"nombre": nombre})


# ---------------- LIBRO ----------------

def obtener_libros():
    return list(libro_col.find())

def insertar_libro(titulo):
    libro_col.insert_one({"titulo": titulo, "ediciones": []})

def actualizar_libro(titulo, nuevo):
    libro_col.update_one(
        {"titulo": titulo},
        {"$set": {"titulo": nuevo}}
    )

def borrar_libro(titulo):
    libro_col.delete_one({"titulo": titulo})


# ---------------- EDICION ----------------

def insertar_edicion(titulo, isbn, anio, idioma):
    libro_col.update_one(
        {"titulo": titulo},
        {
            "$push": {
                "ediciones": {
                    "ISBN": isbn,
                    "año": anio,
                    "idioma": idioma,
                    "copias": []
                }
            }
        }
    )


# ---------------- COPIA ----------------

def insertar_copia(titulo, isbn, numero):
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

# ---------------- USUARIO ----------------

def obtener_usuarios():
    return list(usuario_col.find())

def insertar_usuario(rut, nombre):
    usuario_col.insert_one({"rut": rut, "nombre": nombre})

def actualizar_usuario(rut, nuevo):
    usuario_col.update_one(
        {"rut": rut},
        {"$set": {"nombre": nuevo}}
    )

def borrar_usuario(rut):
    usuario_col.delete_one({"RUT": rut})