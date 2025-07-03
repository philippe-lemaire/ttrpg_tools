from django.contrib import admin
from .models import Monster

# Register your models here.


class MonsterAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "hit_dice", "thac0", "alignment", "source"]
    list_filter = ["source", "thac0", "hit_dice"]


admin.site.register(Monster, MonsterAdmin)
