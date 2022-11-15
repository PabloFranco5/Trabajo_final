from datetime import datetime

import peewee

from app.v1.Utils.db import db
from .user_model import User


class Resumen_viaje(peewee.Model):
    Fecha_servicio = peewee.DateTimeField(default=datetime.now)
    Lugar_Salida = peewee.CharField
    Lugar_Destino = peewee.CharField
    Trayecto = peewee.CharField
    Tiempo_trayecto = peewee.DateTimeField
    Distancia_recorrida = peewee.DateTimeField
    Clima = peewee.DateTimeField
    Username = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db

        