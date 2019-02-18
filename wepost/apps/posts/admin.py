from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from wepost.apps.posts.models import Node

@admin.register(Node)
class NodeAdmin(MPTTModelAdmin):
  pass