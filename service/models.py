from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Ava(models.Model):
    image_1 = models.ImageField(upload_to="service/images/")
    image_2 = models.ImageField(upload_to="service/images/")
    content = models.TextField(verbose_name="Ava Content", blank=True, null=True)

    def __str__(self):
        return f"Ava {self.content}"

    class Meta:
        verbose_name_plural = "Ava Content"

    def clean(self):
        if not self.image_1 and self.image_2:
            raise ValidationError(
                "An image_1 and image_2 is required for the Ava Content."
            )


class WhatWeBring(models.Model):
    image = models.ImageField(
        upload_to="whatwebring/images/", verbose_name="WhatWeBring Image"
    )
    title = models.CharField(max_length=255, verbose_name="WhatWeBring Name")
    description = models.TextField(verbose_name="WhatWeBring Description")

    def __str__(self):
        return self.title


class Services(models.Model):
    image = models.ImageField(upload_to="service/images/", verbose_name="Service Image")
    title = models.CharField(max_length=255, verbose_name="Service Name")
    slug = models.SlugField(
        max_length=255, unique=True, blank=True, verbose_name="Service Slug"
    )
    description = RichTextField(verbose_name="Service Description")

    def __str__(self):
        return f"{self.title} - {self.description[:50]}..."

    class Meta:
        verbose_name_plural = "Services"

    def clean(self):
        if not self.image:
            raise ValidationError(("An image is required for the service."))

    def save(self, *args, **kwargs):
        """
        Ensure a unique slug is generated for the blog.
        Resize and compress the image if it's new or updated.
        """
        # Update slug if title changes
        if (
            not self.slug
            or self.pk is None
            or Services.objects.get(pk=self.pk).title != self.title
        ):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
