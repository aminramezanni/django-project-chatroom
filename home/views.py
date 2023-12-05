from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'home/home.html',context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'home/room.html', context)
