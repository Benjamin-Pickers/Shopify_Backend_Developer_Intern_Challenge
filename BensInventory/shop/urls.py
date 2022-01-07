from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('AddProduct/', views.AddProduct, name='AddProduct'),
]
