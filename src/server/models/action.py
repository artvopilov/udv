from django.db import models
from .user import UdvUser
from .blockOfText import BlockOfText
from .actionType import ActionType
from .statusType import StatusType


class Action(models.Model):
    Id = models.IntegerField(unique=True, primary_key=True)
    Block_of_text_id = models.ForeignKey(BlockOfText, on_delete=models.CASCADE)
    Moderator_src_Id = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1,
                                         related_name="moderator_source")
    Moderator_dst_Id = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=1,
                                         related_name="moderator_destination")
    Action_Type_Id = models.ForeignKey(ActionType, on_delete=models.SET_DEFAULT, default=1)
    Old_version = models.TextField
    New_version = models.TextField
    Status_Id = models.ForeignKey(StatusType, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        app_label = "server"
        db_table = "Action"
