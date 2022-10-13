import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.
def home(request):
    q = request.GET.get('q', '')
    rooms = Room.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for r in rooms:
    #     if r['id'] == int(pk):
    #         room = r
    context = {'room': room}

    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        print(type(form))
        print(type(request.POST))
        form = RoomForm(request.POST)
        print(type(form))
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})