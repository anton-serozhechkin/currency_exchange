from django import forms
from .models import OptionRate, MainRate


class FormMainRate(forms.ModelForm):
    
    uah = forms.DecimalField(max_digits=4, decimal_places=2)
    usd = forms.IntegerField()
    date_of_rate = forms.DateField()    

    class Meta:
        model = MainRate
        fields = ('uah', 'usd', 'date_of_rate')

class FormOptionRate(forms.ModelForm):
    
    uah_purchase = forms.DecimalField(max_digits=4, decimal_places=2)
    uah_sale = forms.DecimalField(max_digits=4, decimal_places=2)
    usd = forms.IntegerField()
    date_of_rate = forms.DateField()    

    class Meta:
        model = OptionRate
        fields = ('uah_purchase', 'uah_sale', 'usd', 'date_of_rate')