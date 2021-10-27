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
    """Custom user model with extended properties that suit our needs"""

    class Meta:
        """Define custom table name for this model"""
        db_table = 'users'

    class UserType(models.TextChoices):
        """Choices for admin site and storage in database"""
        SELLER = 'SL', 'Seller'
        CLIENT = 'CL', 'Client'

    type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.CLIENT)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """String representation of this model"""
        return f'User {self.first_name} {self.last_name}'


class Sale(models.Model):
    """Sales of our business"""

    class Meta:
        """Define custom table name for this model"""
        db_table = 'sales'

    created_at = models.DateTimeField(null=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='client')
    seller = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='seller')

    def __str__(self):
        """String representation of this model"""
        return f'Sale {self.id}'
