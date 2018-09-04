import random

from django.shortcuts import render
from django.template import loader

from minerals.models import Mineral

def index(request):
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'index.html', {'minerals':minerals,
                                          'random_mineral':random_mineral,
                                          'logo':loader.render_to_string('logo.html')})