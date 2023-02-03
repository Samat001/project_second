from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializer
from rest_framework import generics

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
    try:
        title = Music.objects.get(title=title)
    except Music.DoesNotExist:
        return Response('Такой песни нет!')
    serializer = MusicSerializer(title, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_music(request,id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('Нет такой песни!')
    song.delete()
    return Response(f'{song} успешно удалилено !') 

@api_view(['PUT','PATCH'])
def music_update(request, id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('Нет такой песни!')
    if request.method == 'PUT':
        serializer = MusicSerializer(instance=song, data=request.data)
        
    else :
        serializer = MusicSerializer(instance=song,data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(f'успешно обновили:{song}')

class MusicView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer