from django.db import models

# Create your models here.
class Contact1(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
        return self.email
    

    
class Food_data(models.Model):
    mood=models.CharField(max_length=20)
    Main_ing=models.CharField(max_length=50)
    Dish=models.CharField(max_length=100)
    Ing=models.CharField(max_length=1000)
    recipe=models.CharField(max_length=2000)

class Recipe(models.Model):
    image_link = models.CharField(max_length=200)
    ingredients = models.TextField()
    dish = models.CharField(max_length=100)
    recipe = models.TextField()