from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    template = models.TextField()
    template_ru = models.TextField()
    template_kg = models.TextField()
    flight_number = models.CharField(
        max_length=7,
        validators=[RegexValidator(r'^[A-Z]{2,3}\d{1,4}$', 'Invalid flight number format')],
        blank=True,
        null=True,
    )
    origin = models.CharField(
        max_length=3,
        validators=[RegexValidator(r'^[A-Z]{3}$', 'Invalid origin format')],
        blank=True,
        null=True,
    )
    destination = models.CharField(
        max_length=3,
        validators=[RegexValidator(r'^[A-Z]{3}$', 'Invalid destination format')],
        blank=True,
        null=True,
    )
    
    
    def __str__(self):
        return self.name