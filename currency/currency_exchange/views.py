from django.shortcuts import render, redirect
from .models import MainRate
from .forms import FormMainRate
from currency import umessages 

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
    
    main_rate = MainRate.objects.order_by('-date_of_rate')[:10]
    main_rate_today = MainRate.objects.order_by('-date_of_rate')[:1]
    if main_rate:
        context = []        
        context.append({'main_rate': main_rate, 'main_rate_today': main_rate_today})
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
    """
    form = FormMainRate(request.POST or None)
    
    #check form    
    if form.is_valid():
        #list_of_dates = []
        #values_list = MainRate.objects.all().values('date_of_rate')
        #for values in values_list:
         #   print(values)
          #  if values == form.cleaned_data['date_of_rate']:
           #     print('no')
           # else:
            #    print('yes')
            #list_of_dates.append()
        
        form.save()
        form = FormMainRate()
        #after save data in db redirect on main page
        return redirect('main')
    context = {'form': form}
    return render(request, 'currency_exchange/form_main_rate.html', context)