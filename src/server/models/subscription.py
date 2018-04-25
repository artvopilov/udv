from django.db import models
from .user import UdvUser
from .article import Article


class Subscription(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    User_Id = models.ForeignKey(UdvUser, on_delete=models.CASCADE)
    Article_Id = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Subscription"
