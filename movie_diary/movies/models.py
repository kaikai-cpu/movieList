from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),  # Minimum value of 1
            MaxValueValidator(10)   # Maximum value of 10
        ]
    )
    producer = models.CharField(max_length=100)

    def __str__(self):
        return self.title
