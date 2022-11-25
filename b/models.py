from peewee import *

db = SqliteDatabase("database.db")

class Users(Model):
    email = CharField()
    password = CharField()

class Meta:
    Database = db
db.connect()
db.create_tables([])
