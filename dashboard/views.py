from django.shortcuts import render
from django import forms
from .models import *


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

# View form to upload file
def wordlist(request):
    return render(request, 'dashboard/wordlist.html', context)

def uploadWordlist(request):
    # request.FILES
    import pdb; pdb.set_trace()
    pass

# View form to upload file
def stopwords(request):
    return render(request, 'dashboard/stopwords.html', context)

# Upload a stopwords.csv
def uploadStopwords(request):
    # request.FILES
    import pdb; pdb.set_trace()
    pass
