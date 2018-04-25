from django.db import models


class Photo(models.Model):
    link = models.TextField()

    class Meta:
        app_label = "server"
        db_table = "Photo"
