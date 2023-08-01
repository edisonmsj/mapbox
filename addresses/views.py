from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.

class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'addresses/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiZWRpc29ubXNqIiwiYSI6ImNrcGhwaHhsaDBqcjUyb2xpaHB0czVvY3oifQ.xwV3-fok4T9Z6UI9YqUJDQ'
        context ['addresses'] = Address.objects.all

        return context
    