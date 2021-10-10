from django import forms
from django.db import models
from django.db.models import fields

import customer

from .models import Customer


class CreateCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'