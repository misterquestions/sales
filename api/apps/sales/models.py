from django.contrib.auth.models import AbstractUser
from django.db import models

from api.apps.teams.models import Team


class User(AbstractUser):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)


class Sale(models.Model):
    created_at = models.DateTimeField(null=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Sale {self.id}'
