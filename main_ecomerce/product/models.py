from django.db import models


# Create your models here.
class Categories(models.Model):
    categories = models.CharField(max_length=550, default='select')

    def __str__(self):
        return self.categories


class Tag(models.Model):
    tags = models.CharField(max_length=30)

    def __str__(self):
        return self.tags


class Product(models.Model):
    productName = models.CharField(max_length=255, default="Enter the product name")
    productDetails = models.TextField(max_length=3500,
                                      default="Enter product details \nExample:"
                                              " \nProduct Name: \nProduct Id: \nBrand Name \nProduct Categories: \netc")
    productPrice = models.FloatField(default=0)
    productImage = models.ImageField(upload_to='media/productImage')
    productQuantity = models.IntegerField(default=1)
    categories = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tag)
    publishedDate = models.DateTimeField()

    def __str__(self):
        return self.productName
