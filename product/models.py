from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories_per_10g = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name