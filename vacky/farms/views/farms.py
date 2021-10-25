""" Farms views """

# Django 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Models
from vacky.farms.models import Farm

class FarmsView(LoginRequiredMixin, ListView):
    """ Return all farms created """
    template_name = 'farms/index.html'
    model = Farm
    ordering = {'-created',}
    context_object_name = 'farms'