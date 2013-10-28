from django.shortcuts import get_object_or_404, render

from cms.models import Page


def main(request, slug):
    page = get_object_or_404(Page, slug=slug)

    context = {
        'page': page,
    }

    return render(request, 'page.html', context)
