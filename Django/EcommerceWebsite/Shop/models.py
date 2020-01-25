from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60)
    product_image = models.ImageField(upload_to='images')
    product_desc = models.CharField(max_length=300)
    product_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
