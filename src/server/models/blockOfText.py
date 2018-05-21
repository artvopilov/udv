from django.db import models
from .alternativeOpinion import AlternativeOpinion
from .source import Source


class BlockOfText(models.Model):
    text = models.TextField()
    alternative_opinion = models.ForeignKey(AlternativeOpinion, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "block_of_text"
