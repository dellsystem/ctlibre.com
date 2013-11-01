from django.shortcuts import get_object_or_404, render

from cms.models import Page, PageTranslation
from ctlibre.utils import force_slug_language


@force_slug_language(PageTranslation)
def main(request, page):
    context = {
        'page': page,
    }

    return render(request, 'page.html', context)
