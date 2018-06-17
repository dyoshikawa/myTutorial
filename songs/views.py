from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


#songs
def index(request):
    return render(request, 'templates/songs/index.html')
    #return HttpResponse("Hello, world. You're at the songs index.")
