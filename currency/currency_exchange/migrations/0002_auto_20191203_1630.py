# Generated by Django 2.2.6 on 2019-12-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainrate',
            name='author',
        ),
        migrations.RemoveField(
            model_name='mainrate',
            name='uah',
        ),
        migrations.AddField(
            model_name='mainrate',
            name='uah_official',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=5, verbose_name='Rate of ukrainian hryvnia'),
        ),
        migrations.AddField(
            model_name='mainrate',
            name='uah_purchase',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=5, verbose_name='Purchase rate of ukrainian hryvnia'),
        ),
        migrations.AddField(
            model_name='mainrate',
            name='uah_sale',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=5, verbose_name='Sale rate of ukrainian hryvnia'),
        ),
        migrations.DeleteModel(
            name='OptionRate',
        ),
    ]
