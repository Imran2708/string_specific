from django.shortcuts import render
from django.http import HttpResponse


def specific(request):
    return HttpResponse('specific urls')
    
