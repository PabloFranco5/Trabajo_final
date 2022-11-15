
# Contraseña

Primero creamos una instancia de CryptContext y posteriormente 
definimos una función llamada get_password_hash que encriptará 
la contraseña utilizando la instancia de CryptContext que
 acabamos de crear.

La siguiente función se llama create_user y recibe un modelo 
de Pydantic de tipo UserRegister. Esta función se encargará de 
guardar el usuario en la base de datos. Comprobamos si el usuario 
enviado ya existe en la base de datos por email o por username, si es así, 
lanzaremos una excepción HTTPException con el código de estado 400 y
 en el detail explicaremos el porqué del error.

Después usando el modelo de usuario de peewee, creamos el usuario 
con la contraseña encriptada y lo guardamos.

Por último retornamos la información del usuario recién creado 
empleando el modelo User de Pydantic.

# todo_service
