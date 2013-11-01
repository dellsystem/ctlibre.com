from django.contrib import admin
from multilingual_model.admin import TranslationStackedInline

from news.models import Article, ArticleTranslation, Author, AuthorTranslation,\
                        Category, CategoryTranslation


class ArticleTranslationInline(TranslationStackedInline):
    model = ArticleTranslation
    prepopulated_fields = {"slug": ("title",)}


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTranslationInline]


class AuthorTranslationInline(TranslationStackedInline):
    model = AuthorTranslation


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AuthorTranslationInline]


class CategoryTranslationInline(TranslationStackedInline):
    model = CategoryTranslation
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryTranslationInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
