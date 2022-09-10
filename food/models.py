import uuid

from django.db import models

from utils.base_model import BaseModel


class Food(BaseModel):
    name = models.CharField(max_length=256)
    food_groups_choices = {
        ('CARBOHYDRATES', 'CARBOHYDRATES'),
        ('PROTEINS', 'PROTEINS'),
        ('VITAMINS', 'VITAMINS'),
        ('FATS', 'FATS')
    }
    food_group = models.CharField(max_length=32, choices=food_groups_choices)
    description = models.TextField(blank=True, default='')
    quantitation_choices = {
        ('kg', 'kg'),
        ('g', 'g'),
        ('ltr', 'ltr'),
        ('oz', 'oz'),
        ('piece', 'piece'),
        ('packet', 'packet'),
        ('ml', 'ml'),
        ('bunch', 'bunch')
    }
    quantitation = models.CharField(max_length=32, choices=quantitation_choices)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
