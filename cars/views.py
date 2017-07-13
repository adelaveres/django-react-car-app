# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Car

class IndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'cars_list'

    def get_queryset(self):
        return Car.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'

