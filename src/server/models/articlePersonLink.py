from django.db import models
from .personBriefInfo import PersonBriefInfo
from .article import Article


class ArticlePersonLink(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    person_brief = models.ForeignKey(PersonBriefInfo, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "article_person_link"
