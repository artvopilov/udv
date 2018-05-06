from django.db import models
from .common import DbModel


class UdvUser(DbModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    age = models.IntegerField()
    moderator = models.BooleanField(default=False)

    @classmethod
    def insert(cls, first_name, last_name, occupation, age, moderator):
        udv_user = UdvUser(
            first_name=first_name,
            last_name=last_name,
            occupation=occupation,
            age=age,
            moderator=moderator
        )
        UdvUser._insert(udv_user)

    class Meta:
        app_label = "server"
        db_table = "udv_user"
