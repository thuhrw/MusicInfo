from django.db import models
from django.utils import timezone


class Song(models.Model):
    num = models.IntegerField()
    name = models.CharField()
    artist = models.CharField()
    lyric = models.CharField()
    url = models.CharField()
    pic_url = models.CharField()
    artist_url = models.CharField()


class Singer(models.Model):
    num = models.IntegerField()
    name = models.CharField()
    pic_url = models.CharField()
    desc = models.CharField()
    url = models.CharField()


class Comment(models.Model):
    num = models.IntegerField()
    context = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)
