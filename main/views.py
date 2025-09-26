from django.shortcuts import render
from django.http import HttpResponse
from .models import Cont

def home(request):
    contecst = Cont.objects.all()
    return HttpResponse(contecst)
