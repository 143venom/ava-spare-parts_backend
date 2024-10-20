from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CompanyHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyHighlight
        fields = "__all__"


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"


class FeedBackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackForm
        fields = "__all__"
