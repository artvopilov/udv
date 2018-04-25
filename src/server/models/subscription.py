from django.db import models
from .user import UdvUser
from .article import Article


class Subscription(models.Model):
    user = models.ForeignKey(UdvUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Subscription"
