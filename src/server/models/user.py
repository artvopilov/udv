from django.db import models


class UdvUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    age = models.IntegerField()
    moderator = models.BooleanField(default=False)

    class Meta:
        app_label = "server"
        db_table = "User"
