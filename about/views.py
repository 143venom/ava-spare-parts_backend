from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutListViewSet(viewsets.ModelViewSet):
    queryset = AboutList.objects.all()
    serializer_class = AboutListSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
