
# User_model.py

Nuestra base de datos constará de dos tablas, una para almacenar los 
usuarios llamada user y otra tabla llamada todo que almacenará las el
historia detallado de cada busqueda de un usuario.

Esta clase extiende de peewee.Model y en ella declaramos los campos que 
vamos a necesitar que será un email, username y password. El id no es 
necesario definirlo, ya que peewee se encargará de crearlo automáticamente 
como clave primaria y autoincrement.

Después añadimos la clase Meta dentro de la clase User que contendrá la 
conexión a la base de datos.

Viaje_model.py PENDIENTE A COLOCAR LA EXPLICACION DE LA TABLA 