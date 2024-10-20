from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"contact-form", ContactFormViewSet, basename="contact-form")
router.register(r"map", MapViewSet, basename='map')

urlpatterns = [
    path("", include(router.urls)),
]
