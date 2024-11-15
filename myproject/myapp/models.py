from django.db import models

class Client(models.Model):
    ENTITY_TYPE_CHOICES = [
        ('юридична', 'Юридична особа'),
        ('фізична', 'Фізична особа')
    ]

    client_name = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=10, choices=ENTITY_TYPE_CHOICES)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.client_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

class Sale(models.Model):
    PAYMENT_FORM_CHOICES = [
        ('готівковий', 'Готівковий'),
        ('безготівковий', 'Безготівковий')
]
    
    sale_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    payment_form = models.CharField(max_length=15, choices=PAYMENT_FORM_CHOICES)
    delivery_needed = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Sale - {self.client.client_name} - {self.product.product_name}"