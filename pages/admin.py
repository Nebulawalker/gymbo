from django.contrib import admin
from .models import Page, ContentBlock


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    pass
