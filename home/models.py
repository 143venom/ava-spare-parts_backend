from django.db import models
from django.core.exceptions import ValidationError
from core.models import baseModel


# Create your models here.
class Slider(models.Model):
    Active = "A"
    Inactive = "I"
    STATUS_CHOICES = [
        (Active, "Active"),
        (Inactive, "Inactive"),
    ]
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        help_text="Enter the main title for the slider.",
    )
    sub_title = models.CharField(
        max_length=255,
        verbose_name="Subtitle",
        help_text="Enter the subtitle for the slider.",
    )
    image = models.ImageField(
        upload_to="home/sliders/",
        default="default/default_slider.jpeg",
        verbose_name="Slider Image",
        help_text="Upload an image for the slider. Default image will be used if none is provided.",
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default="Active",
        help_text="Status of the Slider",
    )

    class Meta:
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.title

    def clean(self):
        if not self.image:
            raise ValidationError("An image is required for the slider.")


class Brand(models.Model):
    Active = "A"
    Inactive = "I"
    STATUS_CHOICES = [
        (Active, "Active"),
        (Inactive, "Inactive"),
    ]
    name = models.CharField(
        max_length=255,
        verbose_name="company name",
        help_text="Name of the Brane company",
    )
    image = models.ImageField(upload_to="home/brand/")
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default="Active",
        help_text="Status of the Brand",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Brand"

    def clean(self):
        if not self.image:
            raise ValidationError("An image is required for the brand.")


class CompanyHighlight(models.Model):
    icon = models.ImageField(upload_to="home/companyhighlight/")
    title = models.CharField(max_length=255, verbose_name="company highlight title")
    number = models.CharField(max_length=255, verbose_name="company highlight title")

    def __str__(self):
        return f"Company Highlights - {self.title}"

    class Meta:
        verbose_name_plural = "Company Highlight"

    def clean(self):
        if not self.image:
            raise ValidationError("An icon is required for the CompanyHighlight.")


class FeedBack(models.Model):
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback - {self.content}"

    class Meta:
        verbose_name_plural = "Feedback"


class FeedBackForm(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Full Name",
        help_text="Name of the person giving feedback",
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email Address",
        help_text="Email address of the person giving feedback",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone Number",
        help_text="Phone number of the person giving feedback",
    )
    subject = models.CharField(
        max_length=255, verbose_name="Subject", help_text="Subject of the feedback"
    )
    message = models.CharField(
        max_length=255, verbose_name="Message", help_text="Message of the feedback"
    )

    def __str__(self):
        return f"Feedback from {self.name} - {self.subject}"

    class Meta:
        verbose_name_plural = "Feedback Form"
