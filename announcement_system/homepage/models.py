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
    
    def __str__(self):
        return self.name