from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MainRate(models.Model):
    uah_official = models.DecimalField('Rate of ukrainian hryvnia', max_digits=5, decimal_places=3, default='0')
    uah_purchase = models.DecimalField('Purchase rate of ukrainian hryvnia', max_digits=5, decimal_places=3, default='0')
    uah_sale = models.DecimalField('Sale rate of ukrainian hryvnia', max_digits=5, decimal_places=3, default='0')
    usd = models.IntegerField('Number of dollar units', default=1)
    date_of_rate = models.DateField('Date of rate')
    created = models.DateTimeField('Date of creation', default=timezone.now)
    
    def __str__(self):
        return ('Rate, created  {} , official rate: {}').format(self.created, self.uah_official)

    class Meta:
        verbose_name = 'Main rate of currency'
        verbose_name_plural = 'Rates of currency'