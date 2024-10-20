from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "image_preview")  # Display the image preview
    search_fields = ("title", "sub_title")  # Fields to be searched
    ordering = ("title",)  # Default ordering in the list view

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="50" />', obj.image.url
            )
        return "No image"

    image_preview.short_description = "Image Preview"


admin.site.register(Slider, SliderAdmin)
admin.site.register(Brand)
admin.site.register(CompanyHighlight)
admin.site.register(FeedBack)
admin.site.register(FeedBackForm)
