from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    introduction = models.CharField(max_length=1000)
    photo = models.ImageField()
    stock = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"
