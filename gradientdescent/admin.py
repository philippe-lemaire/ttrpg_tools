from django.contrib import admin
from .models import Monarch

# Register your models here.


class MonarchAdmin(admin.ModelAdmin):
    search_fields = ["campaign_name"]
    list_display = ["campaign_name", "current_stress"]


admin.site.register(Monarch, MonarchAdmin)
