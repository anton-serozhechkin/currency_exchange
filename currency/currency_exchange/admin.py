from django.contrib import admin
from .models import *

class MainRateAdmin(admin.ModelAdmin):
    list_display = ('uah', 'usd', 'date_of_rate')
    list_filter = ('date_of_rate', )
    search_fields = ('date_of_rate', )

class OptionRateAdmin(admin.ModelAdmin):
    list_display = ('created', 'uah_purchase', 'uah_sale')
    list_filter = ('created', )
    search_fields = ('created', )

admin.site.register(MainRate, MainRateAdmin)
admin.site.register(OptionRate, OptionRateAdmin)