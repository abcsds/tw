from django.db import models
from twitter_stream.models import AbstractTweet

class SenTweet(AbstractTweet):
    sentiment = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        if self.lang == 'en' or self.lang == u'en':
            super(SenTweet, self).save(*args, **kwargs) # Call the "real" save() method.
        else:
            return

class WordScore(models.Model):
    word      = models.CharField(max_length=200, unique=True)
    score     = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0, null=True)
    def __unicode__(self):
        return self.word + " " + str(self.score)

class StopWord(models.Model):
    word      = models.CharField(max_length=200, unique=True)
    def __unicode__(self):
        return self.word
