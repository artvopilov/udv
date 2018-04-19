from django.db import models
from .article import Article


class HierarchyArticles(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Article_Id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="current_article")
    Article_parent_Id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="parent_article")

    class Meta:
        app_label = "server"
        db_table = "Hierarchy_of_articles"
