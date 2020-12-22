from django.shortcuts import render, HttpResponse
from .models import top_gaming, top_camera, top_office

def top_5_gaming_smartphone(request):
	device_list = top_gaming.objects.all()
	return render(request, './top-5/gaming.html', {"device_list" : device_list})



def top_5_best_camera_smartphone(request):
	# creating model for this
	device_list = top_camera.objects.all()
	return render(request, './top-5/camera.html', {"device_list" : device_list})

def top_5_best_mobiles_for_office_use(request):
	device_list = top_office.objects.all()
	return render(request, './top-5/office.html',{"device_list" : device_list})