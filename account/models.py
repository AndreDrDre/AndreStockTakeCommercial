from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    # one to one relationship one user can have one customer
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(
        default='profilePic.png', null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATAGORY = (('Inverter', 'Inverter'),
                ('MPPT', 'MPPT'),
                ('Montoring', 'Montoring'),
                ('Solar Controller', 'Solar Controller'),
                )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATAGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('Pending', 'Pending'),
              ('Out for delivery', 'Out for delivery'),
              ('Delivered', 'Delivered'))
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)  # one-to-many
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)  # one-to-many
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
