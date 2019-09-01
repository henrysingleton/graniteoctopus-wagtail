from datetime import datetime

from django.db import models
from django.forms.widgets import Select, CheckboxSelectMultiple
from django.utils.timezone import now

from modelcluster.fields import ForeignKey, ManyToManyField, ParentalManyToManyField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextFieldPanel
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


class DiaryEntry(models.Model):
    date = models.DateField(default=now)
    content = RichTextField()

    panels = [
        FieldPanel('date'),
        RichTextFieldPanel('content')
    ]

    def __str__(self):
        return "Dev diary entry for %s" % self.date.__str__()

    class Meta:
        verbose_name = "Dev Diary Entry"
        verbose_name_plural = "Dev Diary Entries"
