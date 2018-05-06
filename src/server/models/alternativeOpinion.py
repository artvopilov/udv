from django.db import models
from .paragraph import Paragraph


class AlternativeOpinion(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, default=None)

    class Meta:
        app_label = "server"
        db_table = "alternative_opinion"
