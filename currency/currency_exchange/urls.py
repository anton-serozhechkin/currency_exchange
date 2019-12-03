from django.urls import path
from . import views

urlpatterns = [
    #path('', views.main, name='main'),
    #path('option-rate', views.option, name='option-view'),
    path('add-rate', views.data_form_mainrate, name='data-form-mainrate')
]