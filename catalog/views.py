from catalog.models import Product
from django.shortcuts import render

def base(request):

    Product_list = Product.objects.all()
    content = {
        'object_list': Product_list,
        'title': 'Каталог',
    }
    return render(request, 'catalog/base.html', content)

def data(request):
    Product_list = Product.objects.all()
    content = {
        'object_list': Product_list,
    }
    return render(request, 'catalog/data.html', content)

def description(request, pk):
    Description_list = Product.objects.get(pk=pk)
    content = {
        'object_list': Description_list,
        'title': 'Описание',
    }
    return render(request, 'catalog/desc.html', content)