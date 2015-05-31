from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^wordlist/', wordlist, name='wordlist'),
    url(r'^uploadWordlist/', uploadWordlist, name='uploadWordlist'),
    url(r'^stopwords/', stopwords, name='stopwords'),
    url(r'^uploadStopwords/', uploadStopwords, name='uploadStopwords'),
]
# update()
