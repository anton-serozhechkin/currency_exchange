from django.shortcuts import render, redirect
from .models import MainRate
from .forms import FormMainRate
from currency import umessages 

def main(request):
    main_rate = MainRate.objects.order_by('-created')
    if main_rate:
        context = []        
        context.append({'main_rate': main_rate})
    else:
        error = umessages.ERROR_DATA_NOT_FOUND
    return render(request, 'currency_exchange/index.html', locals())

def data_form_mainrate(request):
    form = FormMainRate(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormMainRate()
        return redirect('main')
    context = {'form': form}
    return render(request, 'currency_exchange/form_main_rate.html', context)