from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MainRate(models.Model):
    uah = models.DecimalField('Rate of ukrainian hryvnia', max_digits=4, decimal_places=2)
    usd = models.IntegerField('Number of dollar units', default=1) 
    date_of_rate = models.DateField('Date of rate')
    created = models.DateTimeField('Date of creation', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ('Rate, created by {}, {}').format(self.author, self.created)

    class Meta:
        verbose_name = 'Main rate of currency'

class OptionRate(models.Model):
    uah_purchase = models.DecimalField('Purchase rate of ukrainian hryvnia', max_digits=4, decimal_places=2)
    uah_sale = models.DecimalField('Sale rate of ukrainian hryvnia', max_digits=4, decimal_places=2)
    usd = models.IntegerField('Number of dollar units', default=1) 
    date_of_rate = models.DateField('Date of rate')
    created = models.DateTimeField('Date of creation', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ('Rate, created by {}, {}').format(self.author, self.created)

    class Meta:
        verbose_name = 'Option rate of currency(purchase and sale)'