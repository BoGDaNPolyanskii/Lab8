from django.contrib import admin

from django.contrib import admin
from .models import Client, Product, Sale

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sale)
