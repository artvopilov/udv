from django.db import models
from .blockOfText import BlockOfText
from .user import UdvUser


class AlternativeOpinion(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Block_of_text_id = models.ForeignKey(BlockOfText, on_delete=models.CASCADE)
    User_id = models.ForeignKey(UdvUser, on_delete=models.CASCADE)
    Text = models.TextField()

    class Meta:
        app_label = "server"
        db_table = "Alternative_opinion"
