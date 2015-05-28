from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core import serializers


def dashboard(request):
    tweets = []
    for tweet in SenTweet.objects.all():
        if tweet.lang == 'en':
            tweets.append(tweet)
        else:
            # delete object
            pass
    tweets = serializers.serialize("json", tweets, fields=('user_screen_name','text'))
    return HttpResponse(tweets)
