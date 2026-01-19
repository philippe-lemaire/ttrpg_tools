from django.contrib import admin
from .models import Creature

# Register your models here.


class CreatureAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "LVL", "creature_type"]


admin.site.register(Creature, CreatureAdmin)
