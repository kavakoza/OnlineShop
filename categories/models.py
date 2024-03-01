from django.db import models
from constants import NULLABLE


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    image = models.ImageField(upload_to='category', verbose_name='Image', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
