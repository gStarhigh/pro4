from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    """ This view is used to display the home page """
    template_name = "index.html"
