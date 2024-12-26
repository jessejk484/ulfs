from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='sa_home'),
]