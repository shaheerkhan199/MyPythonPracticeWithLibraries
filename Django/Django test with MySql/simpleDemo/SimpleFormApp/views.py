from django.shortcuts import render
from django.http import HttpResponse
from SimpleFormApp.models import User


# Create your views here.

def index(request):
	# return HttpResponse("This is working")
	return render(request,'form.html')

def saveData(request):
	uname = request.GET.get('uname')
	uemail = request.GET.get('uemail')
	upassword = request.GET.get('upassword')
	udob = request.GET.get('udob')
	newUser = User(user_name=uname,user_email=uemail,user_password=upassword,user_dob=udob)
	newUser.save()
	return HttpResponse("Data Saved Successfully")



