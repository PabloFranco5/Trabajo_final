from app.v1.Model.user_model import User
from app.v1.Model.viaje_model import Resumen_viaje

from app.v1.Utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Resumen_viaje])
        