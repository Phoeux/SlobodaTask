from django.db import models


class Review(models.Model):
    shop_link = models.URLField()
    user = models.EmailField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.SmallIntegerField()