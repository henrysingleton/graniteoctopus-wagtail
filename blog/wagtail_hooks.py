from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import DiaryEntry


class DevDiaryAdmin(ModelAdmin):
    model = DiaryEntry
    menu_icon = 'pilcrow'
    list_display = ('date', 'content')
    search_fields = ('date', 'content')


modeladmin_register(DevDiaryAdmin)
