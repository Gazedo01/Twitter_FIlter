from django.shortcuts import render
from django.http import HttpResponse
from . import search
import json

def home(request):
    return render(request, 'App/home.html')

def search_results(request):
    search_results_dict = search.search("#bbb21")
    return render(request, 'App/home.html', {'results' : search_results_dict})
