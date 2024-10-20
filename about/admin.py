from django.contrib import admin
from .models import *


class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "description", "image")
    search_fields = ("title", "subtitle")
    ordering = ("title",)


class AboutListAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "profession", "description", "image")
    search_fields = ("name", "profession")


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ('name', 'position')


admin.site.register(About, AboutAdmin)
admin.site.register(AboutList, AboutListAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
