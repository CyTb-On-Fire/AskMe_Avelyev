from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_GET
from . import models


def paginate(object_list, request, page_address, url, _context: dict, per_page=20):
    paginator = Paginator(object_list, per_page)
    current_page = request.GET.get('page')
    if current_page is None:
        current_page = 1
    page_object = paginator.get_page(current_page)
    _context.update({'page_object': page_object})
    _context.update({'url': url})
    _context.update({'current_page': int(current_page)})
    return render(request, f"{page_address}", context=_context)


def index(request):
    context = {
        'questions': models.QUESTIONS,
    }
    return paginate(models.QUESTIONS, request, 'index.html', '', context)


def ask(request):
    return render(request, 'ask.html')


def question(request, question_id: int):
    context = {
            'answers': models.ANSWERS[question_id][question_id],
            'question': models.QUESTIONS[question_id],
            'question_id': question_id
               }
    return paginate(context['answers'], request, 'question.html', '/question', context)


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def settings(request):
    return render(request, 'settings.html')


