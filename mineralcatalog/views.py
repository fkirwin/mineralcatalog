import random

from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    """Returns the main page with all of the minerals listed."""
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'index.html', {'minerals': minerals, 'random_mineral': random_mineral})
