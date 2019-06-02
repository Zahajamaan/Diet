from django.db import models


class DietType (models.Model):
    name= models.CharField(max_length= 20)
    description= models.TextField(blank=False)
    price= models.DecimalField(max_digits=100, decimal_places=2)


    def __str__(self):
        return self.name