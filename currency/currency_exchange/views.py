from django.shortcuts import render, redirect
from .models import MainRate
from .forms import FormMainRate
from currency import umessages
from django import forms
import datetime


def main(request):
    """
        main view of site

        :param request: standard django param

        **Code**
            
            main_rate - JQuery object with data from model, 
                        ordered by date_of_rate
            error - text message with description of error

            context - list, which contains dict with main_rate as key
    """

    main_rate = MainRate.objects.order_by('-date_of_rate')
    
    if main_rate:
        context = []        
        context.append({'main_rate': main_rate})
    else:
        error = umessages.ERROR_DATA_NOT_FOUND
    return render(request, 'currency_exchange/index.html', locals())
    

def data_form_mainrate(request):
    """
        view form submission

        :param request: standard django param

        **Code**

            form - form on template, which contains fields from model 
            
            context - dict, which contains form as key

            list_of_values - list with values data_of_rate from db
    """
    form = FormMainRate(request.POST or None)
    if request.method == 'POST':
        
        #check form  
        if form.is_valid():

            date_from_form = form.cleaned_data['date_of_rate']

            text = MainRate.objects.all().values('date_of_rate')
            
            list_of_values = []

            #add all existing element in list
            for kl in text:
                list_of_values.append(kl['date_of_rate'])

            if list_of_values:
                for i in list_of_values:
                    #check if date of new rate from form already in db
                    if date_from_form in list_of_values:
                        error = umessages.ERROR_ALREADY_EXIST
                    else:
                        form.save()
                        form = FormMainRate()
                        #after save data in db redirect on main page
                        return redirect('main') 
            else:
                form.save()
                form = FormMainRate()
                #after save data in db redirect on main page
                return redirect('main')
        else:
            error = umessages.ERROR_NOT_VALID
            
    context = {'form': form}
    return render(request, 'currency_exchange/form_main_rate.html', locals())