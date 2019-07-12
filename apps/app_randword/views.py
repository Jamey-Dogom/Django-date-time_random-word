from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    request.session['rand'] = get_random_string(length=14)
    request.session['count'] += 1
    return render(request, "app_randword/index.html")

def reset(request):
    request.session['count'] = 0
    return redirect("/random_word") 