from django.db import models
from django.contrib.auth.models import AbstractUser


class WepostUser(AbstractUser):
  followed_or_blocked = models.ManyToManyField('self',
                                               symmetrical=False,
                                               through='wepost_sns.UserRelation',
                                               through_fields=('from_user', 'to_user'))
