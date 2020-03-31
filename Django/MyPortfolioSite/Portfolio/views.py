from django.shortcuts import render, HttpResponse
from . models import Skill
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def skills(request):
    # Fetching all skills from models and passing it to skill template
    skills = Skill.objects.all()
    data = {'allSkills': skills}
    return render(request, 'skills.html', data)

