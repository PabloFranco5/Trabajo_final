Conexion a la base de datos

# settings.py

la libreria os se usa para  leer las variables de entorno, la clase BaseSettings
y la función load_dotenv de la librería python-dotenv la cual se encargará de leer 
las variables de entorno.

Después declaramos la clase Settings que extenderá de BaseSettings y para finalizar 
declaramos las variables que guardarán la información sobre la conexión y autenticación 
a la base de datos.

Los valores los asignamos gracias a la función getenv de la librería os la cual recibe
el nombre que les dimos a las variables de entorno en el archivo .env y si existen 
retornan su valor. Si no es así, devolverá None.
 
# db.py

Lo que estamos haciendo primero es crear una instancia de clase Settings que creamos 
unos pasos más atrás y después guardar las variables de entorno de la conexión en constantes.

Posteriormente, sobreescribimos la clase PeeweeConnectionState, esto se hace por el 
asincronismo y está mejor explicado en el tutorial de FastAPI que os he dejado en el párrafo 
anterior.

El siguiente paso es efectuar la conexión a la base de datos de PostgreSQL, aquí es donde 
empleamos los parámetros de autenticación y conexión.

Por último, las funciones reset_db_state y get_db las utilizaremos para poder utilizar la 
conexión a la base de datos en todo nuestro proyecto. 