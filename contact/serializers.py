from .serializers import *
from rest_framework import serializers
from .models import *


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"

    def create(self, validated_data):
        return ContactForm.objects.create(**validated_data)


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"
