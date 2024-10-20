from django.contrib import admin
from .models import *


# Register your models here.
class BlogsAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ("title", "author", "status")
    search_fields = ("title", "author")
    list_filter = ("status", "author")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Custom queryset logic can go here if needed
        return qs

    # def get_readonly_fields(self, request, obj=None):
    #     """
    #     Make certain fields read-only if needed.
    #     Adjust the fields list based on your needs.
    #     """
    #     readonly_fields = []
    #     if obj:  # Editing an existing object
    #         readonly_fields = ['slug']  # For example, make the slug read-only
    #     return readonly_fields

admin.site.register(Blogs, BlogsAdmin)
