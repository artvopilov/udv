from django.db import models


class DbModel(models.Model):
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, model_id):
        try:
            return cls.objects.get(id=model_id)
        except:
            return None

    class Meta:
        abstract = True
