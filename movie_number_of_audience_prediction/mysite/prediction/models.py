from django.db import models
import os
import django
from django.db.models.base import Model

# 기본 세팅이다. 꼭 해줘야 한다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# movieCd	movieNm	showTm	audits	nations	directors	movie_img_url
class Movie(models.Model):
    movieCd       = models.CharField(max_length=100)
    movieNm       = models.CharField(max_length=1000)
    showTm        = models.FloatField()
    audits        = models.CharField(max_length=100)
    nations       = models.CharField(max_length=500)
    directors     = models.CharField(max_length=100)
    movie_img_url = models.CharField(max_length=1000)
    score         = models.FloatField(default=0)


    # created_date   = models.DateTimeField()
    # published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed  = True
        db_table = "movie"


class Searchword(models.Model):
    title          = models.CharField(max_length=1000)
    created_date   = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed  = True
        db_table = 'searchword'
