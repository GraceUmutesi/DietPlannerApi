from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from meal_plan.models import MealPlan
from meal_plan.serializers import MealPlanSerializer


class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.filter(is_deleted=False)
    serializer_class = MealPlanSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ('id', 'name', 'created_by', 'created_at', 'edited_at')
    search_fields = ('name', 'created_by')
    ordering_fields = ('name', 'created_at', 'edited_at')

    def destroy(self, request, *args, **kwargs):
        user = request.user
        meal_plan = self.get_object()

        if meal_plan.created_by != user:
            response = {'detail': 'Request forbidden'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        meal_plan.delete()
        return Response({'detail': 'Success'}, status=status.HTTP_200_OK)

