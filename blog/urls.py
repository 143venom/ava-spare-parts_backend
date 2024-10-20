# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'blogs', BlogsViewSet, basename='blogs')

urlpatterns = [
    path('', include(router.urls)),
]