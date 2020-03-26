from django.shortcuts import render, HttpResponse
from .cbot.chatbotpy import runbot
# Create your views here.


def index(request):
    return render(request, 'chatWindow.html')
    # return HttpResponse("Hello from shaheer")


def chat(request):
    # return HttpResponse("This is chatbot test")
    resp = ""
    conv = ""
    if request.POST:
        conv = request.POST.get('conv', '')
        user_input = request.POST.get('user_input', '')

        resp = runbot(user_input)

        conv = conv + "" + str(user_input) + "\n" + "BOT:" + str(resp) + "\n"
    else:
        resp = runbot("Hello! This is shopping assistant how may i help you?")
        conv = "BOT:" + str(resp) + "\n";

    return render(request, 'chatWindow.html', {'conv': conv})
