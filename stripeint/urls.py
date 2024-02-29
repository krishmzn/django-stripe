from django.conf.urls import url
from os import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_View(), name = 'home'),
]
