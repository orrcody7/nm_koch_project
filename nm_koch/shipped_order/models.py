from django.db import models

# Create your models here.

class ShippedOrder(models.Model):
    shopping_cart_id = models.ForeignKey('shopping_cart.id')
    tracking_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name