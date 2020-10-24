from django.shortcuts import render
from django.views.generic import TemplateView

from .models import AboutSpacex


class HomeView(TemplateView):
    template_name = "home.html"


class AboutSpacexView(TemplateView):
    model = AboutSpacex
    template_name = "aboutspacex.html"