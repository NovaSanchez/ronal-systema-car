from django.contrib import admin
from django.urls import path
from base.view import HomePageView

from customer.views import CreateCustomerView, ListCustomerView

urlpatterns = [
    path('', ListCustomerView.as_view(), name='listCustomer'),
    path('create', CreateCustomerView.as_view(), name='createCustomer'),

]