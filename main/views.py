from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "main/index.html")

def survey(request):
    return render(request, "main/survey.html")



# def bodytype_details(request, pk):
#     return HttpResponse()

# def bodyimportant(request):
#     return HttpResponse()

