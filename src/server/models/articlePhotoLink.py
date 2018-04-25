from django.db import models
from .article import Article
from .photo import Photo


class ArticlePhotoLink(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Article_Photo_link"
