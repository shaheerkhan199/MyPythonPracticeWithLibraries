from django.shortcuts import render
from Shop.models import Product
from django.http import HttpResponse
# Create your views here.


def index(request):
    all_products = Product.objects.all()
    data = {
        'products': all_products
    }
    return render(request, 'index.html', data)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

