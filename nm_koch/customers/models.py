from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    businessName = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.name
