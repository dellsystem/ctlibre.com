from django.contrib import admin
from multilingual_model.admin import TranslationStackedInline

from news.models import Article, ArticleTranslation, Author, Category, \
                        CategoryTranslation


class ArticleTranslationInline(TranslationStackedInline):
    model = ArticleTranslation
    prepopulated_fields = {"slug": ("title",)}


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTranslationInline]


class CategoryTranslationInline(TranslationStackedInline):
    model = CategoryTranslation
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryTranslationInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
