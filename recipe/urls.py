from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe.views import RecipeViewSet, RecipeTypeViewSet, FavoriteRecipesViewSet, save_recipe_image

routes = DefaultRouter(trailing_slash=False)

routes.register('recipe-types', RecipeTypeViewSet, basename='recipe_types')
routes.register('recipes', RecipeViewSet, basename='recipes')
routes.register('favorite-recipes', FavoriteRecipesViewSet, basename='favorite_recipes')

urlpatterns = [
    path('', include(routes.urls)),
    path('save-recipe-image', save_recipe_image, name='save_recipe_image')
]
