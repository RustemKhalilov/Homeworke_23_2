from django.shortcuts import render
from catalog.models import Product, Category


def home(request):
    Products = Product.objects.all()
    contex = {"Products": Products}
    return render(request, "products_list.html", contex)


def product_detail(request, pk):
    Product_detal = Product.objects.get(pk=pk)
    contex = {"Products": Product_detal}
    return render(request, "product_detail.html", contex)

def contacts(request):
    return render(request, "shyprocontacts.html")
