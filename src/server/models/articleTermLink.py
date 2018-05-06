from django.db import models
from .term import Term
from .article import Article


class ArticleTermLink(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    class Meta:
        app_label = "server"
        db_table = "article_term_link"
