from peewee import CharField, TextField, IntegerField, SqliteDatabase, Model, ForeignKeyField

db = SqliteDatabase('quotes.db')


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    username = CharField()
    user_id = CharField()


class Quote(BaseModel):
    author = ForeignKeyField(Person, backref='quotes')
    text = TextField()


with db:
    db.connect
    if len(db.get_tables()) == 0:
        db.create_tables([Person, Quote])

