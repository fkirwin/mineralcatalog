import random

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import EmptyResultSet, ObjectDoesNotExist

from .models import Mineral
# Create your views here.


def mineral_detail(request, pk):
    """Get the details of the selected mineral from the user.
    Additional query to get a random mineral. Will be better for the DB than a select all."""
    selected_mineral = get_object_or_404(Mineral, pk=pk)
    try:
        record = random.randint(1, Mineral.objects.count() + 1)
        random_mineral = Mineral.objects.get(pk=record)
    except (EmptyResultSet, ObjectDoesNotExist) as err:
        #Default value in case of emergency!
        print(err)
        random_mineral = get_object_or_404(Mineral.objects.first())
    return render(request, 'detail.html',
                  {'mineral': selected_mineral,
                   'random_mineral': random_mineral})
