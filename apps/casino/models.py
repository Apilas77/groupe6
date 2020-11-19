from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    """Account's model"""

    # username, email, password, {first,last}name are provided by contrib.auth.models.User model
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, verbose_name=_("User")
    )
    solde = models.IntegerField(
        default=0,
    )