from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CompanyHighlightViewSet(viewsets.ModelViewSet):
    queryset = CompanyHighlight.objects.all()
    serializer_class = CompanyHighlightSerializer


class FeedBackViewSet(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer


class FeedBackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedBackForm.objects.all().order_by("-id")
    serializer_class = FeedBackFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        feedback_data = serializer.data
        return Response(
            {
                "success": True,
                "message": "Feedback submitted successfully!",
                "data": feedback_data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
