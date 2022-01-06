from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.template import loader

#Home Page
def index(request):
    return render(request, 'shop/index.html')
