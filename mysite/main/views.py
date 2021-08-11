from django.shortcuts import render
from .models import Tutorial


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'tutorials': Tutorial.objects.all()})

