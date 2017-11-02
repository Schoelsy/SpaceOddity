from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from main_app import models
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    user = User.objects.first()

    properties = user.houses.all()
    total_value = sum([house.price for house in properties])

    planets = models.Planet.objects.all()
    context = {
        'planets': planets,
        'user': User.objects.first(),
        'total_value': total_value
    }
    return render(request, 'index.html', context)


def planet(request, planet_id):
    planet = get_object_or_404(models.Planet, id=planet_id)
    return render(request, 'planet.html', {'planet': planet})


def change_ownership(request, house_id):
    house = get_object_or_404(models.House, id=house_id)
    if house.owner is not None:
        house.owner = None
    else:
        house.owner = User.objects.first()

    house.save()
    
    return redirect('planet', planet_id=house.planet.id)
