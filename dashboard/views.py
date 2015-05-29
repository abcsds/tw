from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.core import serializers
from .models import *

# API for json
# def dashboard(request):
#     tweets = []
#     for tweet in SenTweet.objects.all():
#         if tweet.lang == 'en':
#             tweets.append(tweet)
#         else:
#             # delete object
#             pass
#     tweets = serializers.serialize("json", tweets, fields=('user_screen_name','text'))
#     return HttpResponse(tweets)

def dashboard(request):
    tweets = []
    try:
        for tweet in SenTweet.objects.all():
            if tweet.lang == 'en':
                tweets.append(tweet)
    except SenTweet.DoesNotExist:
        raise Http404("No tweets found: run stream.")
    context = {'tweets': tweets}
    return render(request, 'dashboard/dashboard.html', context)

# # Update all scores
# def updateScores(request):
#     for word in WordScore.objects.all():
#         #update word score
#         pass
#     pass
#
# # Upload a wordlist.csv
# def uploadWordlist(request):
#
#     pass
