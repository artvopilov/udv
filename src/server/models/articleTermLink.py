from django.db import models
from .term import Term
from .article import Article


class ArticleTermLink(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Term = models.ForeignKey(Term, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "Article_Term_link"
