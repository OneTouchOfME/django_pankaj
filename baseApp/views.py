from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
rooms = [
    {'id': 1, 'name': 'pankaj'},
    {'id': 2, 'name': 'kumar'},
    {'id': 3, 'name': 'silolia'}
]


def home(request):
    return render(request, 'home.html')


def room(request, pk):
    context = {'rooms': rooms}
    return render(request, 'baseApp/room.html', context)

def about(request):
    return HttpResponse("baseApp about Page")
