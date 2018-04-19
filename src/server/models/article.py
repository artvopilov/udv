from django.db import models
from .user import UdvUser
from .statusType import StatusType


class Article(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Title = models.CharField(max_length=50)
    Moderator_Id = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1)
    Status_id = models.ForeignKey(StatusType, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        app_label = "server"
        db_table = "Article"
