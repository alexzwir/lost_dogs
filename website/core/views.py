from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import LostPetPointForm
from .models import LostPet

def home(request):
    form = LostPetPointForm()
    return render(request,"home.html",{"form":form})

def saving_lost_pet_pointing_form(request):
    form = LostPetPointForm(request.POST)
    if form.is_valid():
        lost_pet = LostPet(lost_pet_pointing = form.cleaned_data['local'])
        lost_pet.save()
        print(form.cleaned_data['local'])
    return HttpResponseRedirect('/')

