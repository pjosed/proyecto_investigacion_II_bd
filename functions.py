from db import db


#Este archivo hace operaciones con la base de datos y es llamado por el app.py para realizar las operaciones solicitadas por el usuario

autor_col = db["autores"]
libro_col = db["libros"]
usuario_col = db["usuarios"]
prestamo_col = db["prestamos"]
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

def obtener_copias_libros():
    todas_copias = []
    
    for libro in libro_col.find():
        titulo = libro.get("titulo") 
        autor_doc = autor_col.find_one({"libros": titulo})
        autor = autor_doc["nombre"] 

        for ed in libro.get("ediciones",[]):
            isbn = ed.get("ISBN")

            for copia in ed.get("copias", []):
                todas_copias.append({
                    "autor": autor,
                    "libro": titulo,
                    "edicion": isbn,
                    "copia": copia.get("numero")
                })
    return todas_copias
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

def obtener_prestamos(rut):
    list_prestamos = []
    
    for prestamo in prestamo_col.find({"RUT_usuario": rut}):
         isbn = prestamo.get("ISBN")
         libro_doc = libro_col.find_one({"ediciones.ISBN": isbn})
         list_prestamos.append(libro_doc["titulo"])
   
    return list_prestamos
