from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return self.title
