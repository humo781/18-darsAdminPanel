from django.db import models
from django.urls import reverse

from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('products:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('products:delete', args=[self.pk])
