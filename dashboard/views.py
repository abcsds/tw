from django.shortcuts import render, redirect
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
    if request.FILES == {}:
        return render(request, 'dashboard/wordlist.html', { 'error_message' : "File not uploaded; try again."})
    for line in request.FILES['wordlist']:
        term, s  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        model = WordScore(word=term,score=int(s),frequency=0)
        try:
            # import pdb; pdb.set_trace()
            model.validate_unique()
            model.save()
        except:
            continue
    return redirect('dashboard:dashboard')

# View form to upload file
def stopwords(request):
    return render(request, 'dashboard/stopwords.html', {})

# Upload a stopwords.csv
def uploadStopwords(request):
    if request.FILES == {}:
        return render(request, 'dashboard/wordlist.html', { 'error_message' : "File not uploaded; try again."})
    for line in request.FILES['stopwords']:
        model = WordScore(word=line)
        try:
            # import pdb; pdb.set_trace()
            model.validate_unique()
            model.save()
        except:
            continue
    return redirect('dashboard:dashboard')
