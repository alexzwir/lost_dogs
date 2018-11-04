from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse

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

# raw_lost_dogs = LostPet.objects.all()
def list_lost_dogs(request):

    data = {
        "data":raw_lost_dogs,
        "dog 1": {
            "Local 1": "Rua Sararé",
            "Photo":"Minha foto"
        },
        "dog 2": {
            "Local 2": "Rua Guilherme Moura",
            "Photo":"Minha foto"
        },
        "dog 3": {
            "Local 3": "Rua Cardoso de Melo, 1460",
            "Photo":"Minha foto"
        },
    }
    return JsonResponse(data)
