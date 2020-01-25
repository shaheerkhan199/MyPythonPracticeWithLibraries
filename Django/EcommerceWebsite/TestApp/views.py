from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'hello.html')


def contact(request):
    return render(request, 'myContact.html')


def printValues(request):
    data = {
        'name': request.GET.get('uname'),
        'phone': request.GET.get('phone')
    }
    return render(request, 'table.html', data)
