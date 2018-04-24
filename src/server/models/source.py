from django.db import models


class Source(models.Model):
    SOURCE_TYPE_CHOICES = (
        (1, 'Web'),
        (2, 'TextBook')
    )

    Id = models.IntegerField(unique=True, primary_key=True)
    Char_number = models.IntegerField
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Link = models.TextField
    Date_upload = models.DateField
    Source_Type = models.IntegerField(choices=SOURCE_TYPE_CHOICES, default=1)

    class Meta:
        app_label = "server"
