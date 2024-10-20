from rest_framework import serializers
from .models import *


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"
