from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from .shopping_bot import shopping_bot


def render_chat_window(request):
    return render(request, 'chatWindow.html')


def get_bot_response(request):
    user_input = request.GET.get('msg')
    print(user_input)
    bot_response = shopping_bot.get_response(user_input)
    print(bot_response)
    print("For debugging")
    output = {'botResponse': bot_response}
    # return render(request, 'chatWindow.html', output)
    return HttpResponse(bot_response)
