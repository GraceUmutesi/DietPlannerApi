from django.db.models import JSONField
from django.db import models

from utils.base_model import BaseModel


class MealPlan(BaseModel):
    name = models.CharField(max_length=256)
    meals = JSONField(default=list, blank=True)
    """
    Meals format
    [
        {
            "recipe_id": "Recipe uuid (str)",
            "recipe_name": "Recipe name (str)",
            "recipe_image": "Recipe image (str)",
            "day": "Week day (str)",
            "time": "day time (Breakfast, Lunch, Dinner) (str)"
        },
        ...
    ]
    """

    def __str__(self):
        return f'{self.name}'
