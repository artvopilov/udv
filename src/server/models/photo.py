from django.db import models


class Photo(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Link = models.TextField

    class Meta:
        app_label = "server"
        db_table = "Photo"
