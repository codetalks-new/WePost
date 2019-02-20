from django.contrib import admin

# Register your models here.
from wepost.apps.wallets.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
  pass