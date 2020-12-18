from django.contrib import admin

# Register your models here.
from .models import news, Sitemap



admin.site.register(news)
admin.site.register(Sitemap)