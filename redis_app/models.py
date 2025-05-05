from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    
class Animal(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='animals')
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    habitat = models.CharField(max_length=255)
    diet = models.CharField(max_length=255)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name