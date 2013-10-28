from django.core.urlresolvers import reverse
from django.db import models


class Page(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    custom_template = models.BooleanField(default=False)
    graphic = models.ImageField(upload_to='graphics')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cms', args=[self.slug])
