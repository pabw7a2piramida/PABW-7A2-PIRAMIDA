from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobil
# Create your views here.



# Create your views here.
def index(request):
	mobils = Mobil.objects.all()
	return render(request, '/index.html', {'mobils': mobils})