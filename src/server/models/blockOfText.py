from django.db import models
from .paragraph import Paragraph
from .source import Source


class BlockOfText(models.Model):
    Text = models.TextField()
    Paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    Source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Block_of_text"
