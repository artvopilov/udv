from django.db import models
from .common import DbModel
from django.contrib.auth.models import AbstractUser
from django import forms


class UdvUser(DbModel, AbstractUser):
    occupation = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True, blank=True)
    moderator = models.BooleanField(default=False)
    email = models.EmailField(blank=True, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @classmethod
    def insert(cls, password, email, first_name, last_name):
        udv_user = UdvUser(
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            moderator=False
        )
        udv_user.set_password(password)
        udv_user.save()

    class Meta:
        app_label = "server"
        db_table = "udv_user"
