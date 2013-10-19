from django.shortcuts import render

from news.models import Article


def home(request):
    lead_story = Article.objects.get(is_lead_story=True)
    main_stories = Article.objects.get_recent(3)

    context = {
        'lead_story': lead_story,
        'main_stories': main_stories,
    }

    return render(request, 'home.html', context)
