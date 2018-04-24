from django.db import models
from .user import UdvUser


class Article(models.Model):
    STATUS_CHOICES = (
        (1, 'Approved'),
        (2, 'New'),
        (3, 'Changes required'),
    )

    Id = models.IntegerField(unique=True, primary_key=True)
    Title = models.CharField(max_length=50)
    Moderator_Id = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1)
    Status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    class Meta:
        app_label = "server"
