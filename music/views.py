from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializer

@api_view(['GET'])
def get_hello(request):
    # print(dir(request))
    # print(request.data)
    return Response('Hello World!')


@api_view(['GET'])
def get_music(request):
    music = Music.objects.all()
    print(music)
    serializer = MusicSerializer(music, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_song(request,id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('НЕТ ТАКОЙ ПЕСНИ!')    
    print(song)
    serializer = MusicSerializer(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def post_music(request):
    # print(request.data)
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_title(request,title):
    title = Music.objects.get(title=title)

    serializer = MusicSerializer(title, many=False)
    return Response(serializer.data)