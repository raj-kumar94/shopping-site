from django.db import models
from django.contrib.auth.models import Permission,User
from django.conf import settings




# Create your models here.
class Customer(models.Model):

    cust = models.ForeignKey(User, on_delete=models.CASCADE,null=True, default=1)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.phone


class Cart(models.Model):

    cart_cust = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    total = models.IntegerField()
    name = models.CharField(max_length=16, default=1)

    def __str__(self):
        return self.cart_cust.username+ ' - ' + self.name


class BankDetail(models.Model):

    bank_cust = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    name = models.CharField(max_length=16)
    card_no = models.CharField(max_length=16)


    def __str__(self):
        return self.name

class Items(models.Model):

    ITEM_CHOICES = (
        ('Phones', 'phone'),
        ('Laptops', 'laptop'),
        ('Men', 'man'),
        ('Women', 'woman'),
        ('Laptops', 'laptop'),
        ('Cars', 'car'),
        ('Watches', 'watch'),
    )
    item_type = models.CharField(max_length=20, choices=ITEM_CHOICES)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20, null=True)
    price = models.IntegerField(null=True, default=0)
    description = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.item_type+ ' - ' + self.name

