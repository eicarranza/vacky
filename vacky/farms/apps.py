from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FarmsAppConfig(AppConfig):
    name = "vacky.farms"
    verbose_name = _("Farms")
