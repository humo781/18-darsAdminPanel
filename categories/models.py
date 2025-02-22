from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories_images/')

    def get_detail_url(self):
        return reverse('categories:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('categories:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('categories:delete', args=[self.pk])

    def __str__(self):
        return self.name
