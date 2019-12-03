from django.contrib import admin
from .models import *

class MainRateAdmin(admin.ModelAdmin):
    list_display = ('uah', 'usd', 'date_of_rate', 'author')
    #list_editable = ('uah', 'usd')
    list_filter = ('date_of_rate', 'author')
    search_fields = ('date_of_rate', 'author')

class OptionRateAdmin(admin.ModelAdmin):
    list_display = ('created', 'uah_purchase', 'uah_sale', 'author')
    #list_editable = ('uah_purchase', 'uah_sale' )
    list_filter = ('created', 'author')
    search_fields = ('created', 'author')

admin.site.register(MainRate, MainRateAdmin)
admin.site.register(OptionRate, OptionRateAdmin)