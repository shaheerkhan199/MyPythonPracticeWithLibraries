from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60)
    product_image = models.ImageField(upload_to='images')
    product_desc = models.CharField(max_length=300)
    product_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=50)
    customer_phone = models.BigIntegerField()
    customer_password = models.CharField(max_length=15)
    customer_DOB = models.DateField(auto_now=False, auto_now_add=False)
    customer_gender = models.CharField(max_length=6)
    customer_address = models.CharField(max_length=250)

    def __str__(self):
        customer_full_name = self.customer_first_name+" "+self.customer_last_name
        return customer_full_name


