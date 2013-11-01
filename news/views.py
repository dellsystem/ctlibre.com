from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.translation import ugettext as _

from ctlibre.utils import force_slug_language
from news.models import Article, ArticleTranslation, Category, \
                        CategoryTranslation


@force_slug_language(ArticleTranslation)
def article_detail(request, article):
    context = {
        'article':  article
    }

    return render(request, 'article/detail.html', context)


@force_slug_language(CategoryTranslation)
def category_detail(request, category):
    if category is not None:
        article_list = category.article_set.get_recent()
    else:
        article_list = Article.objects.get_recent()

        # Temporary - until I found a better way of storing this
        archives_image = '/media/graphics/spiderweb.jpg'
        archives_name = _('Archives')
        archives_description = _('All articles')

        category = {
            'graphic': {
                'url': archives_image
            },
            'name': archives_name,
            'description': archives_description,
        }

    page_number = request.GET.get('page', 1)
    paginator = Paginator(article_list, 15)
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'articles': articles,
    }

    return render(request, 'category/detail.html', context)
