from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Reg_form
from .models import Registration
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Reg_form(request.POST)
        return HttpResponse("You have registered")
    
    return render(request, 'realapp/index.html', {'form' : Reg_form})

def main_page(request):
    users = Registration.objects.all()
    context = {'users': users}
    return render(request, 'realapp/mainpage.html', context)