from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    # Exclude the 'slug' field from being displayed in the admin form
    exclude = ('slug',)
    
    # Define which fields should be displayed in the list view
    list_display = ('title', 'image_preview')

    # Optionally, you can add search functionality or filters
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="50" />', obj.image.url
            )
        return "No image"

    image_preview.short_description = "Image Preview"

class WhatWeBringAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="50" />', obj.image.url
            )
        return "No image"

    image_preview.short_description = "Image Preview"
    

admin.site.register(Services, ServicesAdmin)
admin.site.register(WhatWeBring, WhatWeBringAdmin)
admin.site.register(Ava)
