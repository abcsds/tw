from django.shortcuts import render, redirect
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
    return render(request, 'dashboard/wordlist.html', {})

def uploadWordlist(request):
    # request.FILES['wordlist']
    # import pdb; pdb.set_trace()
    return redirect('dashboard:dashboard')

# View form to upload file
def stopwords(request):
    return render(request, 'dashboard/stopwords.html', {})

# Upload a stopwords.csv
def uploadStopwords(request):
    # request.FILES['stopword']
    # import pdb; pdb.set_trace()
    return redirect('dashboard:dashboard')
