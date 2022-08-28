from django.urls import path, include
from rest_framework.routers import DefaultRouter

from meal_plan.views import MealPlanViewSet

routes = DefaultRouter(trailing_slash=False)

routes.register('meal-plans', MealPlanViewSet, basename='meal_plans')

urlpatterns = [
    path('', include(routes.urls))
]
