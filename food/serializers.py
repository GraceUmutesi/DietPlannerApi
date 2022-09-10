from rest_framework import serializers

from food.models import Food


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        exclude = ('is_deleted', )

    def to_representation(self, instance):
        serialized_data = super(FoodSerializer, self).to_representation(instance)
        serialized_data['unit_price'] = float(serialized_data['unit_price'])

        return serialized_data
