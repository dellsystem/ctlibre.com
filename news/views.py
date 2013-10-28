from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from news.models import Article, Category


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article':  article
    }

    return render(request, 'article/detail.html', context)


def category_detail(request, slug=None):
    if slug is not None:
        category = get_object_or_404(Category, slug=slug)
        article_list = category.article_set.get_recent()
    else:
        article_list = Article.objects.get_recent()
        category = {
            'graphic': {
                'url': {
                    'media/graphics/cool2.jpg',
                },
            },
            'name': 'Archives',
            'description': 'All the articles, etc',
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
