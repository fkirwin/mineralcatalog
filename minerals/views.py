

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.template import loader

from .models import Mineral
# Create your views here.


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    import os
    cwd = os.getcwd()
    print(cwd)
    return render(request, 'detail.html',
                  {'mineral': mineral, 'logo':loader.render_to_string('logo.html')})

