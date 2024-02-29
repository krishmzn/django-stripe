from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    tempalte_name = 'hotel.html'