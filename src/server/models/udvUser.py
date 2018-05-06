from django.db import models


class UdvUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    age = models.IntegerField()
    moderator = models.BooleanField(default=False)

    @classmethod
    def get_by_id(cls, user_id):
        return cls.objects.get(id=user_id)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        app_label = "server"
        db_table = "udv_user"





