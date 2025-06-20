from django.shortcuts import render

def home(request):
    return render(request, 'miweb/home.html')


def studies(request):
    return render(request, 'miweb/studies.html')

def portfolio(request):
    return render(request, 'miweb/portfolio.html')