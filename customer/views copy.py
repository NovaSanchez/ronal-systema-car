from django.shortcuts import render
from django.views import generic

from .forms import CreateCustomerForm


from .models import Customer


# Create your views here.


class CreateCustomerView(generic.CreateView):

    template_name = "list_customer.html"
    model = Customer
    form_class = CreateCustomerForm


class ListCustomerView(generic.ListView):

    model = Customer
    queryset = Customer.obejcts.all()
    template_name = "list_customer.html"
