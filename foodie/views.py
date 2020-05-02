from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

GNAVI_URL = "https://api.gnavi.co.jp/RestSearchAPI/v3/"
GNAVI_KEY = "xxxxx"


class IndexView(TemplateView):
    template_name = 'foodie/index.html'