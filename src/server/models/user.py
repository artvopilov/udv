from django.db import models


class UdvUser(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=50)
    Age = models.IntegerField()
    Moderator = models.BooleanField(default=False)

    class Meta:
        app_label = "server"
        db_table = "User"
