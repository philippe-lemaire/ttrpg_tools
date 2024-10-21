from django.contrib import admin
from .models import Creature, Variation

# Register your models here.


class VariationInline(admin.StackedInline):
    model = Variation
    extra = 6


class CreatureAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "HP", "STR", "DEX", "WIL"]
    inlines = [VariationInline]


admin.site.register(Creature, CreatureAdmin)
