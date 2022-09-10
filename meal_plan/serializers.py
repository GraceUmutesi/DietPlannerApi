from rest_framework import serializers

from grocery_list.models import GroceryList
from grocery_list.serializers import GroceryListSerializer
from meal_plan.models import MealPlan


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        exclude = ('is_deleted', )

    def to_representation(self, instance):
        serialized_data = super(MealPlanSerializer, self).to_representation(instance)

        grocery_list = GroceryList.objects.filter(meal_plan=instance).first()

        serialized_data['grocery_list'] = None

        if grocery_list:
            serialized_data['grocery_list'] = GroceryListSerializer(grocery_list).data

        return serialized_data

