from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("This is ChatBot Chat App")
    return render(request, 'chatWindow.html')


def render_chat_window(request):
    return render(request, 'chatWindow.html')

