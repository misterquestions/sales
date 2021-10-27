from django.contrib.auth.models import AbstractUser
from django.db import models

from api.apps.teams.models import Team

USER_SELLER = 'SL'
USER_CLIENT = 'CL'

USER_TYPE_CHOICES = [
    (USER_SELLER, 'Seller'),
    (USER_CLIENT, 'Client'),
]


class User(AbstractUser):
    class Meta:
        db_table = 'users'

    type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=USER_CLIENT)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)


class Sale(models.Model):
    class Meta:
        db_table = 'sales'

    created_at = models.DateTimeField(null=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Sale {self.id}'
