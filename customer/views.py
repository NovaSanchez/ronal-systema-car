from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from .forms import CreateCustomerForm


from .models import Customer


# Create your views here.


class CreateCustomerView(generic.CreateView):

    template_name = "create_customer.html"
    model = Customer
    form_class = CreateCustomerForm
    success_url = reverse_lazy('listCustomer')


class ListCustomerView(generic.ListView):

    model = Customer
    queryset = Customer.objects.all()
    template_name = "list_customer.html"
