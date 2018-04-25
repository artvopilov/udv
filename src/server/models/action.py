from django.db import models
from .user import UdvUser
from .blockOfText import BlockOfText


class Action(models.Model):
    STATUS_CHOICES = (
        (1, 'Approved'),
        (2, 'New'),
        (3, 'Changes required'),
        (4, 'Updated')
    )

    ACTION_TYPE_CHOICES = (
        (1, 'Add'),
        (2, 'Delete'),
        (3, 'Change')
    )

    Block_of_text = models.ForeignKey(BlockOfText, on_delete=models.CASCADE)
    Moderator_src = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1,
                                         related_name="moderator_source")
    Moderator_dst = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1,
                                         related_name="moderator_destination")
    Action_Type = models.IntegerField(choices=ACTION_TYPE_CHOICES, default=1)
    Old_version = models.TextField(null=True)
    New_version = models.TextField(null=True)
    Status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    class Meta:
        app_label = "server"
