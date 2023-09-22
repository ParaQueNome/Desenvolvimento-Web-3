
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.natal),
    path('independencia', views.independencia),
    path('tiradentes', views.tiradentes),

]