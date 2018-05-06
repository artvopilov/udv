from django.db import models


class DbModel(models.Model):
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, model_id):
        return cls.objects.get(id=model_id)

    @classmethod
    def _insert(cls, item):
        item.save()

    class Meta:
        abstract = True
