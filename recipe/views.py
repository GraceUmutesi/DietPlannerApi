from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from food.models import Food
from recipe.filters import RecipeFilter
from recipe.models import Recipe, RecipeType, FavoriteRecipes
from recipe.serializers import RecipeSerializer, RecipeTypeSerializer, FavoriteRecipesSerializer


class RecipeTypeViewSet(viewsets.ModelViewSet):
    queryset = RecipeType.objects.filter(is_deleted=False)
    serializer_class = RecipeTypeSerializer
    pagination_class = None
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_fields = ('id', 'name')
    ordering_fields = ('name', 'created_at')

    def destroy(self, request, *args, **kwargs):
        response = {'detail': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(is_deleted=False)
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = RecipeFilter
    search_fields = ('name', 'recipe_type__name', 'estimated_price')
    ordering_fields = ('name', 'recipe_type', 'estimated_price', 'created_at', 'edited_at')

    def create(self, request, *args, **kwargs):
        user = request.user
        request_data = request.data

        if not request_data.get('name') or not request_data.get('recipe_type') or not request_data.get('ingredients') \
                or not request_data.get('directions'):
            return Response({'detail': 'Bad Request'}, status=400)

        if not request_data.get('description'):
            request_data['description'] = ''

        recipe_type = RecipeType.objects.filter(id=request_data.get('recipe_type')).first()
        if not recipe_type:
            return Response({'detail': 'Recipe type not found'}, status=404)

        estimated_price = 0.0
        for ingredient in request_data.get('ingredients'):
            food = Food.objects.filter(id=ingredient['food_id']).first()
            if food:
                food_price = float(food.unit_price) * float(ingredient['quantity'])
                estimated_price = estimated_price + food_price

        recipe = Recipe(
            name=request_data.get('name'),
            recipe_type=recipe_type,
            description=request_data.get('description'),
            ingredients=request_data.get('ingredients'),
            nutritional_value=request_data.get('nutritional_value'),
            directions=request_data.get('directions'),
            estimated_price=estimated_price,
            created_by=user
        )

        recipe.save()

        response_data = RecipeSerializer(recipe).data
        return Response(response_data, status=201)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()

        if recipe.created_by != user:
            response = {'detail': 'Request forbidden'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        recipe.delete()
        return Response({'detail': 'Success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path="user-sys-recipes", name='user-sys-recipes')
    def get_user_sys_recipes(self, request):
        user = request.user

        recipes = Recipe.objects.filter(is_deleted=False, created_by=user) | \
                  Recipe.objects.filter(is_deleted=False, sys_recipe=True)

        response = RecipeSerializer(recipes, many=True).data

        return Response(response, status=200)




@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def save_recipe_image(request):
    request_data = request.data

    if not request_data['recipe_id'] or not request_data['recipe_image']:
        return Response({'detail': 'Bad Request'}, status=400)

    recipe = Recipe.objects.filter(id=request_data['recipe_id']).first()
    if not recipe:
        return Response({'detail': 'Recipe not found'}, status=404)

    recipe.image = request_data['recipe_image']
    recipe.save()

    response_data = RecipeSerializer(recipe).data
    return Response(response_data, status=200)


class FavoriteRecipesViewSet(viewsets.ModelViewSet):
    queryset = FavoriteRecipes.objects.filter(is_deleted=False)
    serializer_class = FavoriteRecipesSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'created_by')
    ordering_fields = ('created_at', 'edited_at')

    def create(self, request, *args, **kwargs):
        user = request.user
        req_data = request.data

        if not req_data.get('recipe'):
            return Response({'detail': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        recipe = Recipe.objects.filter(id=req_data.get('recipe')).first()
        if not recipe:
            return Response({'detail': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)

        favorite = FavoriteRecipes.objects.filter(created_by=user).first()
        if favorite:
            for r in favorite.recipes.all():
                if r == recipe:
                    response_data = FavoriteRecipesSerializer(favorite).data
                    return Response(response_data, status=status.HTTP_201_CREATED)

            favorite.recipes.add(recipe)
            favorite.save()

            response_data = FavoriteRecipesSerializer(favorite).data
            return Response(response_data, status=status.HTTP_201_CREATED)

        favorite = FavoriteRecipes(
            created_by=user
        )
        favorite.save()
        favorite.recipes.add(recipe)
        favorite.save()

        response_data = FavoriteRecipesSerializer(favorite).data
        return Response(response_data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        response = {'detail': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
