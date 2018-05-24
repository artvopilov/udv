from django.db import models
from .alternativeOpinion import AlternativeOpinion
from .source import Source


class BlockOfText(models.Model):
    text = models.TextField()
    alternative_opinion = models.ForeignKey(AlternativeOpinion, on_delete=models.CASCADE, related_name='blocks')
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    number = models.IntegerField()
    is_main = models.BooleanField(default=True)

    @classmethod
    def insert(cls, source, text, alternative_opinion, number):
        block_of_text = BlockOfText(
            source=source,
            text=text,
            alternative_opinion=alternative_opinion,
            number=number
        )
        block_of_text.save()
        return block_of_text

    class Meta:
        app_label = "server"
        db_table = "block_of_text"
