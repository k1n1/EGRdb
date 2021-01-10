from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comments', views.comments),
    path('commentsdelete', views.commentsdelete),
    path('<str:url>/', views.full),
]