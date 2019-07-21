from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.

class Playlist(models.Model):
    movie_title = models.CharField(max_length =420)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.movie_title
    
    def save_playlist(self):
        self.save()