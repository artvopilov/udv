from django.db import models
from .article import Article


class Paragraph(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='paragraphs')
    subtitle = models.CharField(max_length=50)

    class Meta:
        app_label = "server"
        db_table = "paragraph"
