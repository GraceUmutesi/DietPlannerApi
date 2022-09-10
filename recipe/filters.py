from django_filters import rest_framework as filters

from recipe.models import Recipe


class RecipeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="estimated_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="estimated_price", lookup_expr='lte')

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'recipe_type', 'estimated_price', 'created_at', 'edited_at', 'created_by',
                  'created_by__is_staff', 'sys_recipe')
