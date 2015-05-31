from django.shortcuts import render, redirect
from .models import *


def dashboard(request):
    context = {'tweets': SenTweet.objects.all(), 'overall': OverallScore.objects.all()}
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
        return render(request, 'dashboard/stopwords.html', { 'error_message' : "File not uploaded; try again."})
    for line in request.FILES['stopwords']:
        model = WordScore(word=line)
        try:
            # import pdb; pdb.set_trace()
            model.validate_unique()
            model.save()
        except:
            continue
    return redirect('dashboard:dashboard')

def update():
    for tweet in SenTweet:
        if not tweet.sentiment:
            #update sentiment
            pass
