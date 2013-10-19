from django.shortcuts import render, get_object_or_404

from news.models import Article


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article':  article
    }

    return render(request, 'article/detail.html', context)
