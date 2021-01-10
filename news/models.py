from django.db import models
import uuid
from datetime import date 
from ckeditor_uploader.fields import RichTextUploadingField



def upload_folder():
    month = date.today().month
    year = date.today().year
    return str(month) + str(year)

class news(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to=upload_folder(), default=None, null=True)
    news_body = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Title



class Comments_news(models.Model):
    comments_id = models.CharField(max_length=10000)
    user = models.CharField(max_length=10000)
    news_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()



class Sitemap(models.Model):
    sitemap_value = models.TextField()

    def __str__(self):
        return "SITEMAP"