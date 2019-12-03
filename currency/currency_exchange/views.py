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
    context.append({'main_rate': main_rate, 'option_rate': option_rate})
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
    form = FormMainRate()
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        uah = form.cleaned_data['uah']
        usd = form.cleaned_data['usd']
        date_of_rate = form.cleaned_data['date_of_rate']
        post.user = request.user
        post.save()
        form = FormMainRate()
        #return redirect('')
    args = {'form': form}
    return render(request, 'base.html', locals())

def data_form_optionrate(request):
    form = FormOptionRate()
    if request.method == 'POST' and form.is_valid():
        pass


    return render(request, 'currency_exchange/form_option_rate.html', locals())