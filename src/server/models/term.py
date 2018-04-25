from django.db import models


class Term(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Word = models.CharField(max_length=50)
    Definition = models.TextField()

    class Meta:
        app_label = "server"
        db_table = "Term"
