from django.db import models
from .article import Article


class PersonBriefInfo(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    brief_info = models.TextField()

    class Meta:
        app_label = "server"
        db_table = "Person_brief_info"
