from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import ArticleViewSet

routes = DefaultRouter(trailing_slash=False)

routes.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(routes.urls))
]
