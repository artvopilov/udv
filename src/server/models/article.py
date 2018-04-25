from django.db import models
from .user import UdvUser
from .photo import Photo
from .term import Term
# from .personBriefInfo import PersonBriefInfo

class Article(models.Model):
    STATUS_CHOICES = (
        (1, 'Approved'),
        (2, 'New'),
        (3, 'Changes required'),
    )

    title = models.CharField(max_length=50)
    moderator = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=None, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", null=True, default=None, blank=True)

    subscribers  = models.ManyToManyField(UdvUser, related_name='subscriptions')
    photos       = models.ManyToManyField(Photo)
    terms        = models.ManyToManyField(Term)
    persons      = models.ManyToManyField('PersonBriefInfo', related_name='articles')

    class Meta:
        app_label = "server"
