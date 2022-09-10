from django.db.models import JSONField
from django.db import models

from utils.base_model import BaseModel
from food.models import Food


class RecipeType(BaseModel):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return f'{self.name}'


class Recipe(BaseModel):
    name = models.CharField(max_length=256)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.PROTECT)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='recipes', blank=True, null=True)
    ingredients = JSONField(default=list, blank=True)
    """
    Ingredients format
    [
        {
            "food_id": "Food uuid",
            "food_name": "Food name",
            "unit": "Food quantitation unit",
            "quantity": Food quantity (float)
        },
        ...
    ]
    """
    nutritional_value = JSONField(default=list, blank=True)
    """
    Nutritional Value format (example)
    [
        {
            "name": "Calories",
            "unit": "kcal",
            "value": "167"
        },
        ...
    ]
    """
    directions = models.TextField()
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sys_recipe = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.name}'


class FavoriteRecipes(BaseModel):
    recipes = models.ManyToManyField(Recipe, default=list, blank=True)

    class Meta:
        verbose_name_plural = 'Favorite Recipes'

    def __str__(self):
        return f'{self.id}'

# class RecipeImage(BaseModel):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='recipes')
#
#     class Meta:
#         verbose_name_plural = 'Recipes Images'
#
#     def __str__(self):
#         return f'{self.recipe.name}'



