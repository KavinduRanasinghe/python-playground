from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get(request)  :
    return HttpResponse("Hello , world . This is the index view of GetApp")


