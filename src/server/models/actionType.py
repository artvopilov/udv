from django.db import models


class ActionType(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Type = models.CharField(max_length=20)

    class Meta:
        app_label = "server"
        db_table = "Action_Type"
