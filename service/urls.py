# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'service', ServicesViewSet, basename='service')
router.register(r'whatwebring', WhatWeBringViewSet, basename='whatwebring')
router.register(r'ava', AvaViewSet, basename='ava')
# router.register(r'company-info', CompanyInfoViewSet, basename='company-info')
# router.register(r'social-media', SocialMediaViewSet, basename='social-media')
# router.register(r'footer', FooterViewSet, basename='footer')

urlpatterns = [
    path('', include(router.urls)),
]