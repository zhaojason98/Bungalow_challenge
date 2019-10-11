from django.http import HttpResponse
from django.template import loader

from .models import House

def index(request):
    houses_list = House.objects.values_list('id')
    return houses_list

def description(request, zillow_id):
    house = House.objects.get(id=zillow_id)
    return house.getDescription()

def price(request, zillow_id):
    house = House.objects.get(id=zillow_id)
    return house.getPrice()

def estimate(request, zillow_id):
    house = House.objects.get(id=zillow_id)
    return house.getEstimate()

def tax(request, zillow_id):
    house = House.objects.get(id=zillow_id)
    return house.getTax()

def location(request, zillow_id):
    house = House.objects.get(id=zillow_id)
    return house.getLocation()