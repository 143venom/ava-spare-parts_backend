# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'slider', SliderViewSet, basename='slider')
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'company-highlight', CompanyHighlightViewSet, basename='company-highlight')
router.register(r'feed-back', FeedBackViewSet, basename='feed-back')
router.register(r'feed-back-form', FeedBackFormViewSet, basename='feed-back-form')

urlpatterns = [
    path('', include(router.urls)),
]