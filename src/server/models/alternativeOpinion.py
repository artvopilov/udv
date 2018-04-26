from django.db import models
from .blockOfText import BlockOfText
from .user import UdvUser


class AlternativeOpinion(models.Model):
    block_of_text = models.ForeignKey(BlockOfText, on_delete=models.CASCADE)
    user = models.ForeignKey(UdvUser, on_delete=models.CASCADE)
    text = models.TextField(null=True)

    class Meta:
        app_label = "server"
        db_table = "Alternative_opinion"
