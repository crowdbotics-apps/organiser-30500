from django.conf import settings
from django.db import models


class Given(models.Model):
    "Generated Model"
    amountDue = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
        null=True,
        blank=True,
    )
    change = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
        null=True,
        blank=True,
    )
