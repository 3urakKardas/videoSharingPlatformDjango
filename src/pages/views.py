from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def viewIndexPage(request, *args, **kwargs):

    context = {}

    return render(request, "pages/index/index.html", context)

def viewVideoPage(request, *args, **kwargs):

    context = {}

    if request.method == "GET":

        return render(request, "pages/watch/watch.html", context)

    elif request.method == "POST":

        return render(request, "pages/errors/wrongMethod.html", context)


