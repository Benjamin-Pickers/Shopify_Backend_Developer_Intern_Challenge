from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.template import loader
from django.db import connection
import pandas as pd
from datetime import date
from .models import Product

#Home Page
def index(request):

    all_products = Product.objects.all()

    if all_products:
        return render(request, 'shop/index.html', {'all_products':all_products})

    return render(request, 'shop/index.html')

def ProductToExcel(request):

    query = str(Product.objects.all().query)
    df = pd.read_sql_query(query, connection)
    today = str(date.today())

    df.to_excel(r'./ProductInventory.xlsx', index=False)

    with open(r'./ProductInventory.xlsx', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename=ProductInventory-'+today+'.xlsx'
    return response

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
                                  stock=int(form['stock'])
                                       )
            new_product.save()
            return render(request, 'shop/AddProduct.html', {'dataAcceptedMessage':"Product Successfully Added"})


    return render(request, 'shop/addProduct.html')

def RemoveProduct(request):

    if request.method == 'POST':
        form = request.POST

        try:
            product = Product.objects.get(pk=form['name'])
            product.delete()
            return render(request, 'shop/removeProduct.html', {'dataAcceptedMessage':"Product Removed From Inventory"})
        except:
            return render(request, 'shop/removeProduct.html', {'error_message':"Product Could Not Be Removed Because It Does Not Exist"})


    return render(request, 'shop/removeProduct.html')

def FindProduct(request):

    if request.method == 'POST':
        form = request.POST

        try:
            product = Product.objects.get(pk=form['name'])
            return render(request, 'shop/updateProduct.html', {'product':product})
        except:
            return render(request, 'shop/updateProduct.html', {'error_message':"Product Cannot be Updated Because It Does Not Exist"})
    return render(request, 'shop/updateProduct.html')

def UpdateProduct(request):

    if request.method == 'POST':
        form = request.POST

        try:
            product = Product(productname=form['name'],
                              colour=form['colour'],
                              price=form['price'],
                              stock=int(form['stock'])
                             )
            product.save()
            return render(request, 'shop/updateProduct.html', {'dataAcceptedMessage':"Product Successfully Updated"})
        except:
            return render(request, 'shop/updateProduct.html', {'error_message':"Product Could Not be Updated"})

    return render(request, 'shop/updateProduct.html')
