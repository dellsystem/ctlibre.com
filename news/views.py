from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from ctlibre.utils import force_slug_language, make_paginator
from news.models import Article, ArticleTranslation, Author, Category, \
                        CategoryTranslation


def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    articles = make_paginator(author.article_set.get_recent(), request)
    context = {
        'author': author,
        'articles': articles,
        'title': author.name,
        'graphic_source': author.graphic_source,
    }

    return render(request, 'author/detail.html', context)


@force_slug_language(ArticleTranslation)
def article_detail(request, article):
    context = {
        'article':  article,
        'title': article.title,
        'graphic_source': article.graphic_source,
    }

    return render(request, 'article/detail.html', context)


@force_slug_language(CategoryTranslation)
def category_detail(request, category):
    if category is not None:
        article_list = category.article_set.get_recent()
        title = category.name
    else:
        article_list = Article.objects.get_recent()

        # Temporary - until I found a better way of storing this
        title = _('Archives')
        archives_image = '/media/graphics/spiderweb.jpg'
        archives_description = _('All articles')

        category = {
            'graphic': {
                'url': archives_image
            },
            'description': archives_description,
        }

    articles = make_paginator(article_list, request)

    context = {
        'category': category,
        'articles': articles,
        'title': title,
        'graphic_source': category.graphic_source,
    }

    return render(request, 'category/detail.html', context)
