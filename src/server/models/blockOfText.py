from django.db import models
from .paragraph import Paragraph
from .source import Source


class BlockOfText(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Text = models.TextField
    Paragraph_Id = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    Source_Id = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Block_of_text"
