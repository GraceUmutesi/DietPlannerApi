
from django.db import models
from django.db.models import JSONField

from utils.base_model import BaseModel
from meal_plan.models import MealPlan


class GroceryList(BaseModel):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    foods = JSONField(default=list, blank=True)
    """
    [
        {
            "food_id": "Food uuid (str)",
            "food_name": "Food name (str)",
            "quantity": Food quantity (float),
            "unit": "Food unit (str)",
            "estimated_price": Price number (float) 
        }
    ]
    """
    estimated_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.id}'

