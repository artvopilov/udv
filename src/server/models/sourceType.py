from django.db import models


class SourceType(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Type = models.CharField(max_length=20)

    class Meta:
        app_label = "server"
        db_table = "Source_Type"
