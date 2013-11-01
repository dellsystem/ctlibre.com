from django.contrib import admin
from multilingual_model.admin import TranslationStackedInline

from cms.models import Page, PageTranslation


class PageTranslationInline(TranslationStackedInline):
    model = PageTranslation
    prepopulated_fields = {"slug": ("title",)}


class PageAdmin(admin.ModelAdmin):
    inlines = [PageTranslationInline]


admin.site.register(Page, PageAdmin)
