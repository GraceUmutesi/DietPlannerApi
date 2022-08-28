from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from food.models import Food
from grocery_list.models import GroceryList
from grocery_list.serializers import GroceryListSerializer
from meal_plan.models import MealPlan
from recipe.models import Recipe


class GroceryListViewSet(viewsets.ModelViewSet):
    queryset = GroceryList.objects.filter(is_deleted=False)
    serializer_class = GroceryListSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ('id', 'meal_plan', 'estimated_total_price', 'created_at', 'edited_at')
    ordering_fields = ('estimated_total_price', 'created_at', 'edited_at')

    def create(self, request, *args, **kwargs):
        user = request.user
        request_data = request.data

        if not request_data.get('meal_plan'):
            return Response({'detail': 'Bad Request'}, status=400)

        meal_plan = MealPlan.objects.filter(id=request_data.get('meal_plan')).first()
        if not meal_plan:
            return Response({'detail': 'Recipe type not found'}, status=404)

        foods = []
        estimated_price = 0.0
        for meal in meal_plan.meals:
            recipe = Recipe.objects.filter(id=meal['recipe_id']).first()
            if recipe:
                for ing in recipe.ingredients:
                    food = Food.objects.filter(id=ing['food_id']).first()
                    if food:
                        if any(d['food_id'] == str(food.id) for d in foods):
                            fd = [d for d in foods if d['food_id'] == str(food.id)][0]
                            fd_index = foods.index(fd)
                            fd['quantity'] = float(fd['quantity']) + float(ing['quantity'])
                            fd['estimated_price'] = float(fd['estimated_price']) + (float(ing['quantity']) * float(food.unit_price))
                            foods.remove(foods[fd_index])
                            foods.insert(fd_index, fd)
                        else:
                            estimated_price = float(ing['quantity']) * float(food.unit_price)
                            fd = {
                                'food_id': str(food.id),
                                'food_name': food.name,
                                'quantity': ing['quantity'],
                                'unit': str(food.quantitation),
                                'estimated_price': estimated_price
                            }
                            foods.append(fd)

        for fd in foods:
            estimated_price = estimated_price + fd['estimated_price']

        grocery_list = GroceryList(
            meal_plan=meal_plan,
            foods=foods,
            created_by=user
        )

        grocery_list.save()
        response_data = GroceryListSerializer(grocery_list).data
        return Response(response_data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        grocery_list = self.get_object()

        if grocery_list.created_by != user:
            response = {'detail': 'Request forbidden'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        grocery_list.delete()
        return Response({'detail': 'Success'}, status=status.HTTP_200_OK)
