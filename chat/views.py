# chat/views.py
from django.shortcuts import render
from .models import ChatModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
        chat_list = ChatModel.objects.all()
        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'chat_list':chat_list
        })


class ChatCreate(CreateView):
    template_name = 'chat/room.html'
    model = ChatModel
    #fields = ('author', 'content', 'snsimage')
    fields = ('author', 'content')
    success_url = reverse_lazy('room')