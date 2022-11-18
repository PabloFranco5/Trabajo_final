
#from fastapi import FastAPI

#from app.v1.Router.user_router import router as user_router

#app = FastAPI()

#app.include_router(user_router)

from app.v1.Scripts.create_tables import create_tables

create_tables()
#nombre 
#donde estas = medellin
#a donde vas = bogota
 
#en service  hacer un external para llamar las otras funciones 

#primero, extraer campos obligatorios (punto partida, punto llegada)

#segundo, a partir de salida y llegada completar la funcion de trayecto y clima

#tercero, guardar en el json la informacion necesaria de la funcion de trayecto y clima

#cuarto, almacenar en la base de datos la info importante 

#quinto, armar response de la peticion 

