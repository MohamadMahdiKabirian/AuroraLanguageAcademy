from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def listening(request):
    return render(request, 'listening.html')

def reading(request):
    return render(request, 'reading.html')

def writing(request):
    return render(request, '/writing.html')

def speaking(request):
    return render(request, 'speaking.html')

def mock(request):
    return render(request, 'mock.html')

def login(request):
    return render(request, 'login.html')