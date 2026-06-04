from django.db import models
from django.core.validators import MinLengthValidator , MaxValueValidator
import datetime


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):   # اصلاح شد Pruduct → Product
    name_product = models.CharField(max_length=40)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='products/')
    star = models.IntegerField(
        default=0 ,
          validators=[MaxValueValidator(5)]
          )
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=12)

    def __str__(self):
        return self.name_product   # اصلاح شد (قبلاً اشتباه بود)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=255, default='', blank=True)
    phon = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id}"