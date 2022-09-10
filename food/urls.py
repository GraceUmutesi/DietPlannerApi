from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food.views import FoodViewSet

routes = DefaultRouter(trailing_slash=False)

routes.register('foods', FoodViewSet, basename='foods')

urlpatterns = [
    path('', include(routes.urls))
]
