from rest_framework import serializers

from grocery_list.models import GroceryList


class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryList
        exclude = ('is_deleted', )
