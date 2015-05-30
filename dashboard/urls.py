from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^wordlist/', views.wordlist, name='wordlist'),
    url(r'^uploadWordlist/', views.uploadWordlist, name='uploadWordlist'),
    url(r'^stopwords/', views.stopwords, name='stopwords'),
    url(r'^uploadStopwords/', views.uploadStopwords, name='uploadStopwords'),
]
