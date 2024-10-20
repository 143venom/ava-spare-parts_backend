from django.db import models
from core.models import *


class ContactForm(baseModel):
    first_name = models.CharField(
        max_length=100, verbose_name="First Name", help_text="First Name of the sender"
    )
    second_name = models.CharField(
        max_length=100, verbose_name="Second Name", help_text="Second Name of the sender"
    )
    email = models.EmailField(
        verbose_name="Email Address", help_text="Sender's email address"
    )
    message = models.TextField(verbose_name="Message", help_text="The message content")

    def __str__(self):
        return f"Subject: {self.subject}, Name: {self.name}"

    class Meta:
        verbose_name_plural = "Contact Form Entries"
        ordering = ["-id"]


class Map(models.Model):
    map_iframe = models.TextField(
        blank=True,
        null=True,
        verbose_name="Google Maps Iframe",
        help_text="Embed code for Google Maps",
    )

    def __str__(self):
        return "Google Maps Embed"

    class Meta:
        verbose_name_plural = "Map"
