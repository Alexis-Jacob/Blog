import os
from django.db import models
from django.contrib.auth.models import User


class   FileCategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    def __unicode__(self):
        return (self.name)

class   FileUpload(models.Model):
    obj = models.ImageField(upload_to='%Y/%m/%d')
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d', editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    category = models.ForeignKey(FileCategory)

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        
        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (900, 600)
        # Open original photo which we want to thumbnail using PIL's Image
        # object
        
        image = Image.open(self.obj.file)
        # Convert to RGB if necessary
        # Thanks to Limodou on DjangoSnippets.org
        # http://www.djangosnippets.org/snippets/20/
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0)

        # Save to the thumbnail field
        suf = SimpleUploadedFile(os.path.split(self.obj.name)[-1],
                temp_handle.read(), content_type='image/png')
        self.thumbnail.save(suf.name+'.png', suf, save=False)

        # Save this photo instance
        super(FileUpload, self).save()

    class Admin:
        pass

    def __unicode__(self):
        return (self.name)



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
