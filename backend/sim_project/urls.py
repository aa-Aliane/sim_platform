from django.urls import path, include
from rest_framework import routers
from .views import get_context

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('get_context/', get_context, name='get_context')  
]