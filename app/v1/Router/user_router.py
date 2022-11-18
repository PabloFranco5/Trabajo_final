from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import user_schema
from app.v1.Service import user_service

from app.v1.Utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo usuario"
)
def create_user(user: user_schema.UserBase = Body(...)):
    """
    ## Creacion de un nuevo usuario en la app

    ### Args
    la app va a recibir los siguientes datos en el JSON
    - email: un email valido
    - username: un username valido y unico
    - punto de salida: escribe el punto donde te encuentras
    - punto de llegada: escribe el punto hacia donde te quisieras dirigir 

    ### Returns
    - user: User info
    """
    return user_service.create_user(user)