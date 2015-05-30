from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^wordlist/', views.wordlist, name='wordlist'),
    url(r'^stopwords/', views.stopwords, name='stopwords'),
]
