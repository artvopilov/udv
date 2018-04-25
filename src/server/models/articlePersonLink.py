from django.db import models
from .personBriefInfo import PersonBriefInfo
from .article import Article


class ArticlePersonLink(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    Person_brief_id = models.ForeignKey(PersonBriefInfo, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Article_Person_link"
