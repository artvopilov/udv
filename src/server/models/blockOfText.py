from django.db import models
from .paragraph import Paragraph
from .source import Source


class BlockOfText(models.Model):
    text = models.TextField()
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Block_of_text"
