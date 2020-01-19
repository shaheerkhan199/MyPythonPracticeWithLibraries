from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def remove_punctuation(request):
    text = request.GET.get('txt')
    isCountChars = request.GET.get('countchars')
    # print(text)
    if isCountChars == 'on':
        count = 0
        for char in text:
            if char != ' ':
                count += 1
        punctuation = '''!@#$%^&*()-_'+='-*/.`'''
        new_text = ''
        for word in text:
            if word not in punctuation:
                new_text += word
        params = {'newData': new_text, 'countchars': count}
        return render(request, 'punctuation.html', params)
    else:
        punctuation = '''!@#$%^&*()-_'+='-*/.`'''
        new_text = ''
        for word in text:
            if word not in punctuation:
                new_text += word
        params = {'newData': new_text}
        return render(request, 'punctuation.html', params)

