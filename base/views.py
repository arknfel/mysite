from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Room



def index(request):
    return render(request, 'base/home.html')


def room(request, roomId):
    result = Room.objects.filter(id=roomId).first()
    print(result)
    
    if not result:
        return HttpResponseNotFound
    return render(request, 'base/room.html', {'room': result})


def rooms(request):
    result = Room.objects.all().order_by('id')
    print(result)
    return render(request, 'base/rooms.html', {'rooms': result})