from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


def index(request):
    return HttpResponse(render(request, 'index.html'))


def ask(request):
    return render(request, 'ask.html')


def question(request):
    return render(request, 'question.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def settings(request):
    return render(request, 'settings.html')