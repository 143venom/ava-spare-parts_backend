from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all().order_by("-id")
    serializer_class = ServicesSerializer
    lookup_field = "slug"


class WhatWeBringViewSet(viewsets.ModelViewSet):
    queryset = WhatWeBring.objects.all().order_by("-id")
    serializer_class = WhatWeBringSerializer


class AvaViewSet(viewsets.ModelViewSet):
    queryset = Ava.objects.all().order_by("-id")
    serializer_class = AvaSerializer
