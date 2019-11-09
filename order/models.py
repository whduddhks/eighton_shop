from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    register_date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return str(self.user) + str(self.product)

    class Meta:
        db_table = 'order'
