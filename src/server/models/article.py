from django.db import models
from .user import UdvUser


class Article(models.Model):
    STATUS_CHOICES = (
        (1, 'Approved'),
        (2, 'New'),
        (3, 'Changes required'),
    )

    Title = models.CharField(max_length=50)
    Moderator = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=None, null=True)
    Status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    Parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", null=True, default=None, blank=True)

    class Meta:
        app_label = "server"
