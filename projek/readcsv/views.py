from django.shortcuts import render
from .rcsv import *

# Create your views here.

def index(request):
	return render(request, 'index.html', {'rows':rows})