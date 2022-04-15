from django.db import models
from django.contrib.auth.models import Permission, User
from django.urls import reverse

class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genere = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.album_title + ' - '+ self.artist

    
    # make changes
    # python manage.py makemigrations music
    # python manage.py migrate

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) 
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    song_mps = models.FileField(null = True)
    is_favorite = models.BooleanField(default = False)
    
    def __str__(self):
        return self.song_title