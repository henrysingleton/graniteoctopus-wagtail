from django.db import models

from wagtail.admin.edit_handlers import FieldPanel


class MicroBlogPost(models.Model):
    content = models.TextField(max_length=420, blank=True)
    uri = models.URLField(blank=True)
    uri_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, max_length=80)
    image = models.ImageField(blank=True)

    panels = [
        FieldPanel('slug'),
        FieldPanel('content'),
        FieldPanel('uri'),
        FieldPanel('uri_name'),
        FieldPanel('image')
    ]

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Micro Blog Post"
        verbose_name_plural = "Micro Blog Posts"
