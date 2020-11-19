from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    nom = models.CharField(
        unique=True,
        error_messages={
            'unique': _("An application with that name already exists."),
        },
        max_length=128,
    )
    active = models.BooleanField(
        default=False,
        help_text=_(
            'Avoid any errors before the apps has been ready'
        ),
    )