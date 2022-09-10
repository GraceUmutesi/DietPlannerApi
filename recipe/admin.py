from django.contrib import admin

from recipe.models import Recipe, RecipeType, FavoriteRecipes

admin.site.register(RecipeType)
admin.site.register(Recipe)
admin.site.register(FavoriteRecipes)
