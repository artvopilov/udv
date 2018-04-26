from django.db import models
from .article import Article
from .photo import Photo


class ArticlePhotoLink(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Article_Photo_link"
