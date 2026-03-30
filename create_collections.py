from db import db

# Crear colecciones
libros = db["libros"]
autores = db["autores"]
usuarios = db["usuarios"]
prestamos = db["prestamos"]

# Insertar estructura inicial de ejemplo

libros.insert_one({
    "titulo": "Libro A",
    "ediciones": [     #ediciones está embebido dentro de libros, ya que cada libro puede tener varias ediciones, y cada edición tiene sus propios detalles como ISBN, año, idioma y copias disponibles.
        {
            "ISBN": "123456",
            "año": 2020,
            "idioma": "Español",
            "copias": [     #Copias está embebido dentro de ediciones, y es entidad débil (depende de edición)
                {"numero": 1},
                {"numero": 2}
            ]
        }
    ]
})

autores.insert_one({
    "nombre": "Autor ejemplo",
    "libros": ["Libro A", "Libro B"] 
})

usuarios.insert_one({
    "RUT": "12345678",
    "nombre": "Usuario ejemplo"
})

prestamos.insert_one({
    "RUT_usuario": "12345678",
    "ISBN": "123456",
    "numero_copia": 1,
    "fecha_prestamo": "2026-03-29",
    "fecha_devolucion": None
})

print("Colecciones creadas correctamente")