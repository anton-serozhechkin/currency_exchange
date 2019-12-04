from django import forms
from .models import MainRate


class FormMainRate(forms.ModelForm):
    
    uah_official = forms.DecimalField(max_digits=5, decimal_places=3)
    uah_purchase = forms.DecimalField(max_digits=5, decimal_places=3)
    uah_sale = forms.DecimalField(max_digits=5, decimal_places=3)
    usd = forms.IntegerField()
    date_of_rate = forms.DateField()    

    class Meta:
        """
          model - maternal model
          fields - shows in form
        """
        model = MainRate
        fields = ['uah_official',
                  'uah_purchase',
                  'uah_sale',
                  'usd',
                  'date_of_rate'
                ]