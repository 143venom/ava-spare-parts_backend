# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"about", AboutViewSet, basename="about")
router.register(r"about-list", AboutListViewSet, basename="about-list")
router.register(r"team", TeamViewSet, basename="team")
router.register(r"testimonial", TestimonialViewSet, basename="testimonial")

urlpatterns = [
    path("", include(router.urls)),
]
