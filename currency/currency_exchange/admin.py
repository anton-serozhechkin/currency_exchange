from django.contrib import admin
from .models import *

class MainRateAdmin(admin.ModelAdmin):
    list_display = ('uah_official', 'uah_purchase', 'uah_sale', 'usd', 'date_of_rate')
    list_filter = ('date_of_rate', )
    search_fields = ('date_of_rate', )

admin.site.register(MainRate, MainRateAdmin)