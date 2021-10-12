from django.db import models

# Create your models here.

class ShoppingCart(models.Model):
    customer_id = models.ForeignKey('customers.id')
    product = models.ForeignKey('products.product_name')
    price = models.ForeignKey('products.price')
    quantity = models.IntegerField()

    def __str__(self):
        return self.name