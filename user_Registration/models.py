from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from smart_selects.db_fields import ChainedForeignKey
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name="profile")
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
