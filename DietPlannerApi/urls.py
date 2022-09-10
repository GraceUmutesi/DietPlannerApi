"""DietPlannerApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Diet Planner Api",
      default_version='v1',
      description="API for the Diet Planner app",
      contact=openapi.Contact(email="fnissi1004@gmail.com")
   ),
   public=False,
   permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include("rest_framework.urls")),
    # path('api-documentation', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('users.urls'), name='users'),
    path('api/', include('blog.urls'), name='blog'),
    path('api/', include('food.urls'), name='food'),
    path('api/', include('grocery_list.urls'), name='grocery_list'),
    path('api/', include('meal_plan.urls'), name='meal_plan'),
    path('api/', include('recipe.urls'), name='recipe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)