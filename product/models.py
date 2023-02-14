from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='cover/', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    STAR = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'very good'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    star = models.CharField(max_length=20, choices=STAR)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])




