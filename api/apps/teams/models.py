from django.db import models


class Team(models.Model):
    class Meta:
        db_table = 'teams'

    name = models.CharField(max_length=64, null=False)
