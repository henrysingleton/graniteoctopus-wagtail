from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import (
    MicroBlogPost)

class MicroBlogAdmin(ModelAdmin):
    model = MicroBlogPost
    menu_icon = 'pilcrow'
    list_display = ('content', 'uri', 'uri_name', 'image')
    search_fields = ('content', 'uri', 'uri_name', 'image')

modeladmin_register(MicroBlogAdmin)