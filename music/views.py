from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import Album, Song


def index(request):
    print('index')
    all_albums = Album.objects.all()

    return render(request, 'music/index.html', {"all_albums": all_albums})


def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    #
    # except Album.DoesNotExist:
    #     raise Http404('Album does not exit')
    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'music/details.html', {"album": album})

    # return JsonResponse({"name": album.album_title, "artist": album.artist})


def favorite(request, album_id):

    album = get_object_or_404(Album, pk=album_id)
    # print(album_id ,': ',album, ':',album.song_set.get(pk=request.POST['song']))
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
        print(selected_song)
    except (KeyError, Song.DoesNotExist):
        print("exception")
        return render(request, 'music/details.html', {
            'album': album,
            'error_message': 'You did not selected a valid song',
        })
    else:

        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})


