from django.shortcuts import render

def home(request):
    return render(request, 'miweb/home.html')
