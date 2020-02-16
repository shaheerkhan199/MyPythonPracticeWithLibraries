from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

shopping_bot = ChatBot(
        "My Shopping Bot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter"
    )

#Now we are not using list trainer any more
trainer = ChatterBotCorpusTrainer(shopping_bot)
trainer.train("chatterbot.corpus.english")

def index(request):
    # return HttpResponse("This is ChatBot Chat App")
    return render(request, 'chatWindow.html')


def render_chat_window(request):
    return render(request, 'chatWindow.html')


def get_bot_response(request):
    user_input = request.GET.get('msg')
    print(user_input)
    bot_response = shopping_bot.get_response(user_input)
    print(bot_response)
    output = {'botResponse': bot_response}
    return render(request, 'chatWindow.html', output)
