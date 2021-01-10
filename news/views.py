from django.shortcuts import render, HttpResponse, redirect
from .models import news, Comments_news
from django.views.decorators.csrf import csrf_exempt
import uuid


def index(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        return render(request, './error/404.html')


def full(request, url):
    if request.method == 'GET':
        comments_post = Comments_news.objects.filter(news_id=url)
        data = news.objects.filter(url=url).first()
        more = news.objects.all().order_by('?')[:10]
        if data:
            return render(request, "./news.html", {"news": data, "comments_post": comments_post, "more": more})
        else:
            return render(request, './error/404.html')
    else:
        return render(request, './error/404.html')


@csrf_exempt
def comments(request):
    if request.method == 'POST':
        user = str(request.POST['user'])
        news_id = str(request.POST['news_id'])
        display_name = str(request.POST['display_name'])
        comment = str(request.POST['comment'])
        Comments_news(comments_id=str(uuid.uuid4()), user=user, news_id=news_id, display_name=display_name,
                      comments=comment).save()
        return HttpResponse("Your comment add successfully")
    else:
        return render(request, './error/404.html')


@csrf_exempt
def commentsdelete(request):
    if request.method == 'POST':
        news_id = request.POST['news_id']
        user = request.POST['user']
        id = request.POST['id']
        Comments_news.objects.filter(id=id, news_id=news_id).first().delete()
        return HttpResponse("Your comment add successfully")
    else:
        return render(request, './error/404.html')
