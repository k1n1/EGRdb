from django.urls import path
from . import views
from . import top5
urlpatterns = [
    path("", views.index),
    path("mobiles/", views.mobiles),
    path('comments', views.comments),
    path('commentsdelete', views.commentsdelete),
    path('newreview', views.new_reviews),
    path('updatereview', views.update_reviews),
    path("top-5-gaming-smartphone/", top5.top_5_gaming_smartphone),
    path("top-5-best-camera-smartphone/", top5.top_5_best_camera_smartphone),
    path("top-5-best-mobiles-for-office-use/", top5.top_5_best_mobiles_for_office_use),
    path("mobiles/<str:brand>/", views.brand),
    path("<str:url>/", views.full),


]