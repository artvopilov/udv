from django.db import models
from .udvUser import UdvUser
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

    block_of_text = models.ForeignKey(BlockOfText, on_delete=models.CASCADE)
    changer = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1, related_name='changer')
    moderator_checker = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1,
                                          related_name='moderator_checker')
    action_type = models.IntegerField(choices=ACTION_TYPE_CHOICES, default=1)
    old_version = models.TextField(null=True)
    new_version = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    class Meta:
        app_label = "server"
        db_table = "action"
