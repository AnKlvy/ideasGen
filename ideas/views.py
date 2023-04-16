import time

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

import openai
import os

from ideas.forms import ContGener

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]


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
    if request.method == 'POST':
        form = ContGener(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            prompt = f"Make short, funny and meaningless idea using this keywords: {form.cleaned_data['keywords']}."

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                # n=1,
                # stop=None,
                temperature=1,
            )
            message = response.choices[0].text.strip()
            # return redirect('generated', message)
            print(message)
            return render(request, 'ideas/generated.html', {'message': message})

    else:
        form = ContGener()

    return render(request, 'ideas/contgener.html', {'form': form})
    # return redirect('generated', {'form': form})

# keywords = 'gold fabric consumer productivity tvshow'
# print(contgener(keywords))
# redirect ispolzovat
# naiti sposob perenapravit message na sgeneririvannuyu stranicu
