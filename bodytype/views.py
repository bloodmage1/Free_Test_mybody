from django.shortcuts import render

def bodytype(request):
    return render(request, "bodytype/your_constitution.html")
