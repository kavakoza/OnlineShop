from django.db import models
from constants import NULLABLE
from categories.models import Category
from django.conf import settings


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='Image', **NULLABLE)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='Category', **NULLABLE)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Seller')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
