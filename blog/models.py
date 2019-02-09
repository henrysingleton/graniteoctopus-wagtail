from datetime import datetime

from django.db import models
from django.forms.widgets import Select, CheckboxSelectMultiple

from modelcluster.fields import ForeignKey, ManyToManyField, ParentalManyToManyField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet

class DefaultDateField(models.DateField):
    def get_default(self):
        return datetime.now

class BlogPage(Page):
    date = DefaultDateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', blocks.TextBlock(template='blog/blocks/code.html',
                                  icon='code')),
        ('image', ImageChooserBlock()),
    ])

    category = ForeignKey('blog.BlogCategory', null=True, blank=True,
                          on_delete=models.DO_NOTHING)

    related = ParentalManyToManyField('blog.BlogPage', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('category', widget=Select),
        FieldPanel('related', widget=CheckboxSelectMultiple)
    ]

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"