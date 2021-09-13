from django.contrib   import admin
from django.urls      import path
from django.conf.urls import include

import prediction.views

urlpatterns = [
    path('', prediction.views.MovieView.get, name="get"),
    path('post', prediction.views.MovieView.post, name="post"),
]