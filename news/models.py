from django.db import models
from django_thumbs.db.models import ImageWithThumbsField

from news.fields import UniqueBooleanField
from news.constants import GRAPHIC_SIZES


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class ArticleManager(models.Manager):
    def get_recent(self, n):
        return self.filter(is_lead_story=False).order_by('-created_on')[:n]


class Article(models.Model):
    objects = ArticleManager()
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    slug = models.SlugField()
    graphic = ImageWithThumbsField(upload_to='graphics', sizes=GRAPHIC_SIZES)
    is_lead_story = UniqueBooleanField()

    def __unicode__(self):
        return "%s by %s [%s]" % (self.title, self.author, self.category)
