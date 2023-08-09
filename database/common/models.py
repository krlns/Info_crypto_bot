from datetime import datetime

import peewee as pw

database = pw.SqliteDatabase("rating_coins.db")


class ModelBase(pw.Model):
    create_at = pw.DateField(default=datetime.now())

    class Meta:
        database = database


class History(ModelBase):
    name_coin = pw.TextField()
    numbers_of_cliks = pw.IntegerField()
