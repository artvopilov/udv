from django.db import models


class Source(models.Model):
    SOURCE_TYPE_CHOICES = (
        (1, 'Web'),
        (2, 'TextBook')
    )

    char_number = models.IntegerField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    link = models.TextField()
    date_upload = models.DateField()
    source_type = models.IntegerField(choices=SOURCE_TYPE_CHOICES, default=1)

    class Meta:
        app_label = "server"
        db_table = "source"
