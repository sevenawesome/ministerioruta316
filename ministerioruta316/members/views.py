from django.shortcuts import render
from django.http import HttpResponse


def show_index(request):
    return render(request,'member/index.html',{"name":'Salim Bencosme'})
