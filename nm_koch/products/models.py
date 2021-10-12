from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=500)
    price = models.IntegerField()
    unit_of_issue = models.CharField(max_length=100)

    def __str__(self):
        return self.name