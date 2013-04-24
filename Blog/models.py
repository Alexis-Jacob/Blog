from django.db import models
from django.contrib.auth.models import User

class   Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    def __unicode__(self):
        return (self.name)

class   Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(User)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")
    validated = models.BooleanField(default=False)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return (u"%s" % self.title)

class   Comment(models.Model):
    author = models.CharField(max_length=20)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return (self.author)


# class   FileUpload(models.Model):
#     name = models.CharField()
#     file = models.FileField()
#     url  = models.URLField()
