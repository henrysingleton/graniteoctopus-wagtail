from __future__ import unicode_literals

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page

from blog.models import BlogPage


class HomePage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['posts'] = BlogPage.objects.descendant_of(self).live().order_by('-date')

        return context

