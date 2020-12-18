from django.shortcuts import render, HttpResponse
from django.db.models import Q
from mobiles.models import *

def search(request):
	quary = request.GET['search']
	search_result = None
	search_result = samsung.objects.filter(Q(Name__icontains = quary))
	print(search_result)
	return render(request, './search/search.html', {'search_result' : search_result})