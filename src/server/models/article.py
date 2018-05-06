from django.db import models
from .udvUser import UdvUser
from .photo import Photo
from .term import Term


class Article(models.Model):
    STATUS_CHOICES = (
        (1, 'Approved'),
        (2, 'New'),
        (3, 'Changes required'),
    )

    creator = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=None, null=True,
                                related_name="articles_creator")
    title = models.CharField(max_length=50)
    moderator = models.ForeignKey(UdvUser, on_delete=models.SET_DEFAULT, default=None, null=True,
                                  related_name="articles_moderator")
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", null=True, default=None,
                               blank=True)
    subscribers = models.ManyToManyField('Subscription', related_name='articles')
    photos = models.ManyToManyField(Photo)
    terms = models.ManyToManyField(Term)
    persons = models.ManyToManyField('PersonBriefInfo', related_name='articles')

    @classmethod
    def get_by_moderator_id(cls, user_id):
        return cls.objects.get(moderator=user_id)

    class Meta:
        app_label = "server"
        db_table = "article"
