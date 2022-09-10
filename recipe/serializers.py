from rest_framework import serializers

from recipe.models import Recipe, RecipeType, FavoriteRecipes


class RecipeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeType
        exclude = ('is_deleted', )


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ('is_deleted', )

    def to_representation(self, instance):
        serialized_data = super(RecipeSerializer, self).to_representation(instance)
        serialized_data['recipe_type'] = RecipeTypeSerializer(instance.recipe_type).data

        return serialized_data


class FavoriteRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipes
        exclude = ('is_deleted', )

    def to_representation(self, instance):
        serialized_data = super(FavoriteRecipesSerializer, self).to_representation(instance)
        serialized_recipes = []

        if len(serialized_data['recipes']) > 0:
            for recipe_id in serialized_data['recipes']:
                recipe = Recipe.objects.filter(id=recipe_id).first()
                serialized_recipes.append(RecipeSerializer(recipe).data)

        serialized_data['recipes'] = serialized_recipes

        return serialized_data

