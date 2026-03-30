from db import db
from functions_consola import *

# Colecciones
libro_col = db["libro"]
autor_col = db["autor"]
usuario_col = db["usuario"]
prestamo_col = db["prestamo"]

# -------------------------------
# MENU PRINCIPAL
# -------------------------------

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. CRUD Autor, Libro, Edicion y Copia")
        print("2. CRUD Usuario")
        print("3. CRUD Prestamo")
        print("4. Consultas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud_libro_autor()

        elif opcion == "2":
            crud_usuario()

        elif opcion == "3":
            crud_prestamo()

        elif opcion == "4":
            consultas()

        elif opcion == "5":
            break


# -------------------------------
# EJECUTAR
# -------------------------------

if __name__ == "__main__":
    menu()