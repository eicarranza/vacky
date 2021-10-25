""" Farms urls. """

# Django 
from django.urls import include, path

# Views
from .views import farms as farm_views


urlpatterns = [
    path(
        route='',
        view=farm_views.FarmsView.as_view(),
        name='farms'
    )
]
