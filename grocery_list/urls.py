from django.urls import path, include
from rest_framework.routers import DefaultRouter

from grocery_list.views import GroceryListViewSet

routes = DefaultRouter(trailing_slash=False)

routes.register('grocery-lists', GroceryListViewSet, basename='grocery_lists')

urlpatterns = [
    path('', include(routes.urls))
]
