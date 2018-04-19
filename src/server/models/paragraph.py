from django.db import models
from .article import Article


class Paragraph(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Article_Id = models.ForeignKey(Article, on_delete=models.CASCADE)
    Subtitle = models.CharField(max_length=50)

    class Meta:
        app_label = "server"
        db_table = "Paragraph"
