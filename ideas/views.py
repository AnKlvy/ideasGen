from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'ideas/index.html')


def loading_page(request):
    delay = 2  # delay in seconds
    generated = reverse('generated')
    return render(request, 'ideas/loading.html', {'delay': delay, 'generated': generated})


def generated(request):
    return render(request, 'ideas/generated.html')
