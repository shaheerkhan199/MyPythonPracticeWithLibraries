from django.shortcuts import render
from Shop.models import Product, Customer
from django.http import HttpResponse
import time
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


def save_customer_data_on_signup(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    new_customer = Customer(customer_first_name = first_name, customer_last_name = last_name, customer_email = email, customer_phone = phone, customer_password = password, customer_DOB = dob, customer_gender = gender, customer_address = address)
    #
    # try:
    #     match = Customer.objects.get(customer_email=email)
    # except Customer.DoesNotExist:
    #     # Unable to find a user, this is fine
    #     return HttpResponse('Email Already exist')
    # else:
    #     new_customer.save()
    #     return HttpResponse('Data Inserted Successfully')
    match = Customer.objects.get(customer_email=email)
    if match:
        return HttpResponse('Email Already exist')
    else:
        new_customer.save()
        return HttpResponse('Data Inserted Successfully')


def product_details(request, p_id):
    details_of_click_product = Product.objects.get(pk=p_id)
    data = {
        'product_details': details_of_click_product
    }
    return render(request, 'productDetails.html', data)

