from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from wepost.apps.auth.models import WepostUser


class WepostUserAdmin(UserAdmin):
  pass

admin.site.register(WepostUser,WepostUserAdmin)
