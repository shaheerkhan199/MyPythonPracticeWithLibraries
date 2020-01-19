from django.http import HttpResponse
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))


def index(request):
    data = open(os.path.join(BASE, "simpleData.txt"))
    return HttpResponse(data.read())


def about(request):
    return HttpResponse("This is about section")


def favourite_links(request):
    display = '''
            <a href='https:www.facebook.com'>Facebook</a> <br/>
            <a href='https:www.youtube.com'>Youtube</a> <br/>
            <a href='https:www.stackoverflow.com'>Stack Overflow</a> <br/>
        '''
    return HttpResponse(display)
