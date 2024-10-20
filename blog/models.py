from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from core.models import *
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys
from django.core.exceptions import ValidationError
import os
from datetime import datetime


class Blogs(models.Model):
    ACTIVE = "A"
    INACTIVE = "I"
    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    ]

    title = models.CharField(max_length=255, verbose_name="Blog Title")
    author = models.CharField(max_length=255, verbose_name="Blog Author")
    content = RichTextField(blank=True, null=True, verbose_name="Blog Content")
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name="Blog Slug",
    )
    image = models.ImageField(upload_to="images/blog/posts", verbose_name="Blog Image")
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=ACTIVE,
        help_text="Select the status of the blog post",
    )
    conclusion = models.TextField(blank=True, null=True, verbose_name="Blog Conclusion")

    def __str__(self):
        return f"{self.title} by {self.author} ({self.get_status_display()})"

    class Meta:
        verbose_name_plural = "Blog"

    def clean(self):
        """
        Ensure that the blog has an image.
        """
        if not self.image:
            raise ValidationError("An image is required for the blog.")

    def save(self, *args, **kwargs):
        """
        Ensure a unique slug is generated for the blog.
        Resize and compress the image if it's new or updated.
        """
        # Update slug if title changes
        if not self.slug or self.pk is None or Blogs.objects.get(pk=self.pk).title != self.title:
            self.slug = slugify(self.title)
        
        # Resize and compress image
        if self.image and isinstance(self.image, InMemoryUploadedFile):
            img = Image.open(self.image)
            target_size = (800, 800)
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            img_io = BytesIO()
            img_format = img.format if img.format else "JPEG"
            quality = 85
            img.save(img_io, format=img_format, quality=quality)
            img_io.seek(0)
            while img_io.tell() > 3 * 1024 * 1024 and quality > 10:
                img_io = BytesIO()
                quality -= 5
                img.save(img_io, format=img_format, quality=quality)
                img_io.seek(0)
            self.image = InMemoryUploadedFile(
                img_io,
                "ImageField",
                self.image.name,
                f"image/{img_format.lower()}",
                sys.getsizeof(img_io),
                None,
            )

        super().save(*args, **kwargs)