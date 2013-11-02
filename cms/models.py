from django.core.urlresolvers import reverse
from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation


class Page(MultilingualModel):
    custom_template = models.BooleanField(default=False)
    graphic = models.ImageField(upload_to='graphics')
    graphic_source = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cms', args=[self.slug])


class PageTranslation(MultilingualTranslation):
    parent = models.ForeignKey(Page, related_name='translations')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('parent', 'language_code')
