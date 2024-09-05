from django.shortcuts import render
from django.http import HttpResponse

def inquires(request):
    return render(request, "inquires/inquire.html")
