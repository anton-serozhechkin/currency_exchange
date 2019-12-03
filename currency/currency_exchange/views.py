from django.shortcuts import render, redirect
from .models import MainRate,  OptionRate
from .forms import FormMainRate, FormOptionRate
from currency import umessages 

def main(request):
    try:
        main_rate = MainRate.objects.order_by('-created')
    except Exception:
        error = umessages.ERROR_FORM_COURSE

    context = []
    context.append({'main_rate': main_rate})
    return render(request, 'currency_exchange/index.html', locals())

def option_rate(request):
    try:
        option_rate = OptionRate.objects.order_by('-created')
    except Exception:
        error = umessages.ERROR_FORM_COURSE
    context = []
    context.append({'option_rate': option_rate})
    return render(request, 'currency_exchange/option_rate.html', locals())

def data_form_mainrate(request):
    form = FormMainRate(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormMainRate()
        #return redirect('')
    context = {'form': form}
    return render(request, 'currency_exchange/form_main_rate.html', context)

def data_form_optionrate(request):
    form = FormOptionRate(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormOptionRate()
        #return redirect('')
    context = {'form': form}
    return render(request, 'currency_exchange/form_option_rate.html', context)