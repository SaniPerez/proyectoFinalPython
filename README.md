PROYECTO FINAL - Iniciación a la Programación con Python.
====================================================================================================

Autor: Sani Dalila Pérez Palacio.
Instructor: José Montezuma
Tutor: Agustina Bianchi 
Comisión: 26209

## Descripción.

Sistema de Gestión de Productos e Inventario desarrollado en Python, utilizando SQLite como base de datos.

El sistema permite realizar las siguientes operaciones:

1. Agregar productos:
	Registrar nuevos productos con nombre, descripción, categoría, cantidad y precio.
2. Mostrar productos:
	Mostrar todos los productos almacenados en la base de datos.
3. Buscar productos:
	Buscar un producto específico utilizando su ID.
4. Actualizar productos:
	Modificar nombre, descripción, categoría, cantidad o precio.
5. Eliminar productos:
	Eliminar un producto de la base de datos, previa confirmación.
6. Reporte de stock mínimo:
	Mostrar los productos cuya cantidad sea igual o inferior al límite indicado.


## Estructura del proyecto.

principal.py: menú principal y control del programa.

operaciones.py: interacción con el usuario, validaciones y lógica.

consultas_sql.py: operaciones SQL sobre los productos.

base_datos.py: conexión a SQLite y creación de la tabla.

inventario.db: base de datos donde se guardan los productos.


## Github - nombre del repositorio.
https://github.com/SaniPerez/proyectoFinalPython.git


