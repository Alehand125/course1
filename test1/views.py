from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(requiest, name, surname):
    return HttpResponse("hello " + name + " " + surname)


def summa(requiest, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)
# dsfgfdsg
# dfsgdfsgdfsgsdfg
