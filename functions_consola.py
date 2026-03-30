from db import db

libro_col = db["libro"]
autor_col = db["autor"]
usuario_col = db["usuario"]
prestamo_col = db["prestamo"]

def crud_libro_autor():
    while True:
        print("\n--- CRUD AUTOR / LIBRO / EDICION / COPIA ---")
        print("1. Autor")
        print("2. Libro")
        print("3. Edición")
        print("4. Copia")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        # ---------------- AUTOR ----------------
        if opcion == "1":
            print("\n1. Insertar Autor")
            print("2. Actualizar Autor")
            print("3. Borrar Autor")
            sub = input("Seleccione: ")

            if sub == "1":
                nombre = input("Nombre del autor: ")
                autor_col.insert_one({"nombre": nombre})
                print("Autor insertado")

            elif sub == "2":
                nombre = input("Autor a actualizar: ")
                nuevo = input("Nuevo nombre: ")
                autor_col.update_one(
                    {"nombre": nombre},
                    {"$set": {"nombre": nuevo}}
                )
                print("Autor actualizado")

            elif sub == "3":
                nombre = input("Autor a borrar: ")
                autor_col.delete_one({"nombre": nombre})
                print("Autor eliminado")

        # ---------------- LIBRO ----------------
        elif opcion == "2":
            print("\n1. Insertar Libro")
            print("2. Actualizar Libro")
            print("3. Borrar Libro")
            sub = input("Seleccione: ")

            if sub == "1":
                titulo = input("Titulo: ")
                libro_col.insert_one({"titulo": titulo, "ediciones": []})
                print("Libro insertado")

            elif sub == "2":
                titulo = input("Libro a actualizar: ")
                nuevo = input("Nuevo titulo: ")
                libro_col.update_one(
                    {"titulo": titulo},
                    {"$set": {"titulo": nuevo}}
                )
                print("Libro actualizado")

            elif sub == "3":
                titulo = input("Libro a borrar: ")
                libro_col.delete_one({"titulo": titulo})
                print("Libro eliminado")

        # ---------------- EDICION ----------------
        elif opcion == "3":
            print("\n1. Insertar Edición")
            sub = input("Seleccione: ")

            if sub == "1":
                titulo = input("Libro: ")
                isbn = input("ISBN: ")
                año = input("Año: ")
                idioma = input("Idioma: ")

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
                print("Edición agregada")

        # ---------------- COPIA ----------------
        elif opcion == "4":
            print("\n1. Insertar Copia")
            sub = input("Seleccione: ")

            if sub == "1":
                titulo = input("Libro: ")
                isbn = input("ISBN: ")
                numero = int(input("Numero copia: "))

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
                print("Copia agregada")

        elif opcion == "5":
            break




def crud_usuario():
    # aca va el segundo punto
    pass


def crud_prestamo():
    # aca va el tercer punto
    pass


def consultas():
    # aca va el cuarto punto
    # consulta 1
    # consulta 2
    pass