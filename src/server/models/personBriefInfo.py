from django.db import models
from .article import Article


class PersonBriefInfo(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Date_of_birth = models.DateField
    Date_of_death = models.DateField
    Brief_info = models.TextField

    class Meta:
        app_label = "server"
        db_table = "Person_brief_info"
