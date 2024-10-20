from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.filter(status=Blogs.ACTIVE).order_by('-id')
    serializer_class = BlogsSerializer
    lookup_field = 'slug'