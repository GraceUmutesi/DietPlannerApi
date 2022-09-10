from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from food.models import Food
from food.serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(is_deleted=False)
    serializer_class = FoodSerializer
    pagination_class = None
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filterset_fields = '__all__'
    search_fields = ['name', 'food_group']
    ordering_fields = '__all__'

    def destroy(self, request, *args, **kwargs):
        response = {'detail': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

