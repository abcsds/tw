from django.db import models
from twitter_stream.models import AbstractTweet

class SenTweet(AbstractTweet):
    sentiment = models.IntegerField(default=0)


class WordScore(models.Model):
    word      = models.CharField(max_length=200)
    score     = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0)
    def __unicode__(self):
        return [self.word, self.score, frequency]
