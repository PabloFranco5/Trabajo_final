import peewee

from app.v1.Utils.db import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    telefono = peewee.CharField()

    class Meta:
        database = db

