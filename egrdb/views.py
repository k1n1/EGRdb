from django.shortcuts import render, redirect, HttpResponse
from news.models import news, Sitemap
import os


def contact(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        name = request.POST["name"]
        subject = request.POST["subject"]
        print(user_id, name, subject)
        return render(request, './contact.html', {"messages" : "Thankyou for your Feedback"})
    else:
        return render(request, './contact.html')

def about(request):
    return render(request, './about.html')


def sitemap(request):
    # news_list = news.objects.all().order_by('-date')
    sitemap_value = Sitemap.objects.all().first()
    return render(request, './sitemap.xml', {"map" : sitemap_value})



def privacy_policy(request):
    return render(request, './pp.html')

def robot(request):
    return render(request, './robot.txt')


def bug(request):
    return render(request, './bug.html')
