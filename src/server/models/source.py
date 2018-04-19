from django.db import models
from .sourceType import SourceType


class Source(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Char_number = models.IntegerField
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Link = models.TextField
    Date_upload = models.DateField
    Source_Type_Id = models.ForeignKey(SourceType, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        app_label = "server"
        db_table = "Source"
