from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'ideas/index.html')


def loading_page(request):
    # simulate some long-running task
    import time
    time.sleep(2)

    # redirect to the destination page
    return redirect(reverse('generated'))


def generated(request):
    return render(request, 'ideas/generated.html')
