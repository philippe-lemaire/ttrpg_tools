from django.contrib import admin

# Register your models here.
from .models import Bounty


class BountyAdmin(admin.ModelAdmin):
    search_fields = ["target", "bounty_level", "location"]
    list_display = ["target", "bounty_level", "location"]


admin.site.register(Bounty, BountyAdmin)
