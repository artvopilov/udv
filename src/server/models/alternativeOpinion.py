from django.db import models
from .blockOfText import BlockOfText
from .user import UdvUser


class AlternativeOpinion(models.Model):
    Block_of_text = models.ForeignKey(BlockOfText, on_delete=models.CASCADE)
    User = models.ForeignKey(UdvUser, on_delete=models.CASCADE)
    Text = models.TextField(null=True)

    class Meta:
        app_label = "server"
        db_table = "Alternative_opinion"
