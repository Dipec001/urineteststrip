from django.urls import path
from . import views

urlpatterns = [
    path('api/uploadimage/', views.ColorIdentificationView.as_view(), name='image-upload'),
    path('', views.index, name='index'),
    ]