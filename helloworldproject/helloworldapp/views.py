from django.shortcuts import render
from django.http import HttpResponse

def helloworldappview(request):
    return HttpResponse('app is called!')

