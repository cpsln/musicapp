from django.db import models


# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' : ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


# ForeignKey means each Song link with Album
'''on_delete = model.CASCADE means that like RED pk1 is Album we want to delete and a Song is a part of Album 
then if delete Album Red the any Song link to this its automatically delete'''

# we make some change music model in django database
# run $ python manage.py makemigarations music
