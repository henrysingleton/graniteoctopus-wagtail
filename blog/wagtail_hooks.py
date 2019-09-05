from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import DiaryEntry


class DevDiaryAdmin(ModelAdmin):
    model = DiaryEntry
    menu_icon = 'pilcrow'
    list_display = ('date', 'html_output')
    search_fields = ('date', 'content')


modeladmin_register(DevDiaryAdmin)
