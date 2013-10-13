from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return "%s by %s [%s]" % (self.title, self.author, self.category)
