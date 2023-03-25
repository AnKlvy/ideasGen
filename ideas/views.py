import time

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView


# Create your views here.

class IdeasHome(ListView):
    template_name = 'ideas/ideasgen.html'

    def get_queryset(self):
        return None


def loading_page(request):
    delay = 4  # delay in seconds
    generated = reverse('generated')
    return render(request, 'ideas/loading.html',
                  {'delay': delay, 'generated': generated})


def generated(request):
    return render(request, 'ideas/generated.html')


def contgener(request):
    return render(request, 'ideas/contgener.html')
