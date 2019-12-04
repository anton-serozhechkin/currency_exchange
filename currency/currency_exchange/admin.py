from django.contrib import admin
from .models import *

class MainRateAdmin(admin.ModelAdmin):
    
    """
    Overview admin's panel

        list_display - list, includes all that will be shows
        list_filter - list items available for filtering by them
        search_fields - search in db for an item in the list
    
    """
    
    list_display = ('uah_official', 'uah_purchase', 'uah_sale', 'usd')
    list_filter = ('date_of_rate', )
    search_fields = ('date_of_rate', )

admin.site.register(MainRate, MainRateAdmin)