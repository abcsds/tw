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
                text = tweet.text

                # Sentiment analisis
                try:
                    for stopWord in StopWord.objects.all():
                        text = text.replace(stopWord.word," ")
                        # import pdb; pdb.set_trace()
                    words = text.split(" ")
                    tweetScore = 0
                    for word in words:
                        for obj in WordScore.objects.all():
                            if word == obj.word:
                                tweetScore += obj.score
                    tweet.sentiment = tweetScore
                except:
                    tweet.sentiment = 0
            else:
                tweet.delete()
    except SenTweet.DoesNotExist:
        raise Http404("No tweets found: run stream.")
    context = {'tweets': tweets}
    return render(request, 'dashboard/dashboard.html', context)

# # Upload a wordlist.csv
# def uploadWordlist(request):
#
#     pass

# # Upload a stopwords.csv
# def uploadStopwords(request):
#
#     pass
