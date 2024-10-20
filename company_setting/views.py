from rest_framework import viewsets
from .models import *
from .serializers import *


class SiteLogoViewSet(viewsets.ModelViewSet):
    queryset = SiteLogo.objects.all().order_by("-id")
    serializer_class = SiteLogoSerializer


class CompanyInfoViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all().order_by("-id")
    serializer_class = FooterSerializer
