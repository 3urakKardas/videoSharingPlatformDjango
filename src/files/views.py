import os

from django.shortcuts import render
from django.http import HttpResponse

from wsgiref.util import FileWrapper
# Create your views here.

def sendFile(request, fileName, *args, **kwargs):
    #script_dir = os.path.dirname(__file__)
    #p = os.path.join(script_dir, "static/" + str(fileName))
    #file = FileWrapper(open(p, 'rb'))
    #response = HttpResponse(file, content_type='text/css')

    profix = fileName.split(".")[1]

    script_dir = os.path.dirname(__file__)

    p = os.path.join(script_dir, "static/" + profix + "/" + str(fileName))

    file = FileWrapper(open(p, 'rb'))
    response = HttpResponse(file, content_type='text/css')

    return response
