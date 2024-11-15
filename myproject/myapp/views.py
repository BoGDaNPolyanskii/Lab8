from django.shortcuts import render
from .models import Client, Sale, Product
def index(request):
    client = Client.objects.all()
    sale = Sale.objects.all()
    print(client)
    product = Product.objects.all()
    return render(
    request,
    "index.html",
    {
        "clients": client,
        "sales": sale,
        "products": product,
    }
)