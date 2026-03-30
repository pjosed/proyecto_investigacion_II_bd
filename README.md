# proyecto_investigacion_II_bd

Proyecto Investigación II - Bases de Datos No Relacionales

## 📌 Descripción

Este proyecto tiene como objetivo el diseño e implementación de una base de datos NoSQL a partir de un modelo relacional proporcionado. Se desarrolla una aplicación web utilizando Python y Flask, con MongoDB como sistema de base de datos, permitiendo gestionar la información mediante operaciones CRUD y consultas específicas.

El proyecto forma parte del curso de Bases de Datos, donde se busca comprender las diferencias entre modelos relacionales y no relacionales, así como aplicar conceptos de modelado y diseño de datos.

## 🎯 Objetivos

* Convertir un modelo entidad-relación a modelo relacional
* Transformar el modelo relacional a un modelo NoSQL
* Implementar la base de datos en MongoDB
* Desarrollar una API con Flask
* Realizar operaciones CRUD
* Ejecutar consultas sobre la base de datos

## 🛠️ Tecnologías utilizadas

* Python 3
* Flask
* MongoDB
* PyMongo
* VS Code
* Git & GitHub

## 📂 Estructura del proyecto

```
proyecto_investigacion_II/
│
├── app.py
├── config.py
├── models/
├── routes/
├── database/
├── requirements.txt
├── README.md
└── venv/
```

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear entorno virtual

```
python -m venv venv
```

### 3. Activar entorno virtual

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

### 4. Instalar dependencias

```
pip install -r requirements.txt
```

### 5. Ejecutar MongoDB

Asegúrate de tener MongoDB corriendo en:

```
mongodb://localhost:27017
```

### 6. Ejecutar la aplicación

```
python app.py
```

## 🚀 Funcionalidades

* Conexión a MongoDB
* Inserción de datos
* Consulta de registros
* Actualización de documentos
* Eliminación de datos
* Modelado NoSQL basado en el diseño relacional

## 📊 Modelo de datos

El modelo de datos fue diseñado inicialmente como un modelo entidad-relación, posteriormente transformado a modelo relacional y finalmente adaptado a MongoDB utilizando colecciones y documentos embebidos.

## 📖 Conceptos aplicados

* Modelo relacional
* Modelo NoSQL
* MongoDB
* Documentos embebidos
* Referencias
* CRUD
* API REST
* Flask

## 📅 Curso

Bases de Datos

## 📄 Licencia

Este proyecto es únicamente con fines académicos.

