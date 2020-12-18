from django.contrib import admin
from django.urls import path, include
from . import views, search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("robot.txt", views.robot),
    path('search/', search.search),
    path('sitemap/', views.sitemap),
    path('contact/', views.contact),
    path('privacy-policy/', views.privacy_policy),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    path('account/', include("authentication.urls")),
    path('news/', include("news.urls")),
    path('bug', views.bug),
    path('', include("mobiles.urls")),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


