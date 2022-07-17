from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='supplied_products')  # просто связал таблицы
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
