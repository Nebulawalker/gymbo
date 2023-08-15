from django.contrib import admin
from .models import Page, ContentBlock, Impression


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    pass

@admin.register(Impression)
class ImpressionAdmin(admin.ModelAdmin):
    # Для тестов
    list_display = ['id', 'page', 'content_block', 'quantity']
    list_filter = ['content_block']
    ordering = ['quantity']
