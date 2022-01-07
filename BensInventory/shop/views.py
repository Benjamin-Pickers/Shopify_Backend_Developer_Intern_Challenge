from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.template import loader

from .models import Product

#Home Page
def index(request):
    return render(request, 'shop/index.html')

def AddProduct(request):

    if request.method == 'POST':
        form = request.POST

        try:
            product = Product.objects.get(pk=form['name'])
            return render(request, 'shop/AddProduct.html', {'error_message':"Product already exists in inventory"})
        except:
            new_product = Product(productname=form['name'],
                                  colour=form['colour'],
                                  price=form['price'],
                                  stock=form['stock']
                                       )
            new_product.save()
            return render(request, 'shop/AddProduct.html', {'dataAcceptedMessage':"Product Successfully Added"})


    return render(request, 'shop/addProduct.html')
