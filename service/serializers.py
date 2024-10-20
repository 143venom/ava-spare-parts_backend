from .models import *
from .serializers import *
from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class WhatWeBringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeBring
        fields = "__all__"


class AvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ava
        fields = "__all__"
