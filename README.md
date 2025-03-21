# technical_test
## Prueba Técnica para Desarrollador Jr


### Parte 2: Ejercicios Prácticos
Los ejercicios se encuentran divididos cada uno en una rama distinta que llevan los nombres de "Django", "Python", "api" y "MySQL". Cada rama contiene la actividad correspondiente al área.
#### 1. Django
#### *Crea un modelo Django para una aplicación de biblioteca con las siguientes características: Libros (título, autor, fecha de publicación) y Autores (nombre, fecha de nacimiento).*
Para la creación de este modelo utilicé Postgres como base de datos, en el archivo settings.py en la línea 77 encontrarán la configuración para la base de datos, donde tiene como nombre ‘library’, el usuario es ‘postgres’ y dejé la contraseña como ‘root’ para no utilizar mi contraseña personal.
Se utilizó el comando ‘pip install psycopg2’ para que la base de datos funcionara de manera correcta.
Podrán encontrar el código escrito en /PruebaDjango/library/library_app/models.py, podrán notar que se hizo una migración para comprobar que el modelo y la migración funcionaban correctamente.

#### 2. Python
#### *Escribe una función en Python que reciba una lista de números y devuelva una nueva lista con los números ordenados de menor a mayor.*
#### *Escribe un script en Python que lea un archivo de texto y cuente la cantidad de palabras que contiene.*
Se creó un proyecto aparte para esta actividad, en él se encuentran dos archivos, uno llamado ‘list.py’ y otro llamado ‘read_text.py’ en donde se realiza la segunda.
-	list.py: Al correr este script se le pide al usuario que ingrese la cantidad de números que quiere listar, posteriormente se le pide que agregue cada uno de los números y al final los imprime ordenados como se indica.
-	read_text.py: Aquí se abre un archivo .txt que también se encuentra en la carpeta del proyecto y se cuentan las palabras, separadas por espacios.

#### 3. MySQL
#### *Escribe una consulta MySQL para crear una tabla llamada “Usuarios” con los campos “id”, “nombre”, “email” y “fecha_de_registro”.*
#### *Inserta tres registros en la tabla “Usuarios”.*
Las consultas se encuentran en un archivo .sql listas para ejecutar.
#### 4. API
#### *Diseña una API simple en Django que permita realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un recurso llamado “Tareas”. Proporciona los endpoints necesarios.*
Para la creación del api, la base de datos tiene una configuración similar, se puede encontrar a partir de la línea 78 y tiene como nombre ‘homework’.
Se utilizaron vistas sencillas que proporciona el framework, los endpoints son los siguientes: 
-	/api/tareas/: proporciona el crear un registro y mostrar todos los registros.
-	/api/tareas/{id}/: proporciona mostrar un registro con determinado identificador, editar y eliminar el mismo registro.

#### Tiempo
-	Parte 1: Para las preguntas teóricas, me demoré alrededor de 40 minutos.
-	Parte 2: Para las pruebas en código me tardé entre 2 hrs y media y 3 hrs tomando descansos entre cada prueba.

