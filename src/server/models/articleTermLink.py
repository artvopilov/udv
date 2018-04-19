from django.db import models
from .term import Term
from .article import Article


class ArticleTermLink(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Article_Id = models.ForeignKey(Article, on_delete=models.CASCADE)
    Term_Id = models.ForeignKey(Term, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Article_Term_link"
