""" Farms models. """

# Django
from django.db import models

# Utilities
from vacky.utils.models import VackyModel

class Farm(VackyModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self):
        return '{} located {}'.format(self.name, self.address)