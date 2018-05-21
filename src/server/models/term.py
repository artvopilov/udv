from django.db import models


class Term(models.Model):
    word = models.CharField(max_length=50)
    definition = models.TextField()

    class Meta:
        app_label = "server"
        db_table = "term"
