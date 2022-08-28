from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import AuthenticationView

routes = DefaultRouter(trailing_slash=False)

routes.register("authentication", AuthenticationView, basename="authentication")

urlpatterns = [
    path("", include(routes.urls)),
]

