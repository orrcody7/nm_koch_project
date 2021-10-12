from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer

# Create your views here.

def index(request):
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }
    return render(request, 'customers/index.html', context)