from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404

def index(request):
    return render(request, 'index.html')