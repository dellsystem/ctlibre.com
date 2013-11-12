from django.core.urlresolvers import reverse
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from multilingual_model.models import MultilingualModel, MultilingualTranslation

from news.fields import UniqueBooleanField
from news.constants import GRAPHIC_SIZES


class Author(MultilingualModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    graphic = models.ImageField(upload_to='graphics')
    graphic_source = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[self.slug])


class AuthorTranslation(MultilingualTranslation):
    parent = models.ForeignKey(Author, related_name='translations')
    bio = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('parent', 'language_code')

    def __unicode__(self):
        return self.get_language_code_display()


class Category(MultilingualModel):
    graphic = models.ImageField(upload_to='graphics')
    graphic_source = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[self.slug])


class CategoryTranslation(MultilingualTranslation):
    parent = models.ForeignKey(Category, related_name='translations')
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        unique_together = ('parent', 'language_code')

    def __unicode__(self):
        return self.get_language_code_display()


class ArticleManager(models.Manager):
    def get_recent(self, n=0, show_lead_story=True):
        if show_lead_story:
            articles = self
        else:
            articles = self.filter(is_lead_story=False)

        articles = articles.order_by('-created_on')

        if n > 0:
            return articles[:n]
        else:
            return articles


class Article(MultilingualModel):
    objects = ArticleManager()
    author = models.ForeignKey(Author)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    graphic = ImageWithThumbsField(upload_to='graphics', sizes=GRAPHIC_SIZES)
    graphic_source = models.URLField(blank=True, null=True)
    is_lead_story = UniqueBooleanField()

    def __unicode__(self):
        return "%s by %s [%s]" % (self.title, self.author, self.category)

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])


class ArticleTranslation(MultilingualTranslation):
    parent = models.ForeignKey(Article, related_name='translations')
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    slug = models.SlugField()

    class Meta:
        unique_together = ('parent', 'language_code')

    def __unicode__(self):
        return self.get_language_code_display()
