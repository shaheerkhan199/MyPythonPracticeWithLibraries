from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("This is my personal portfolio site")
    return render(request, 'index.html')
