from django.shortcuts import render
from .models import *

def search(request):
	return render(request, './search/search.html')