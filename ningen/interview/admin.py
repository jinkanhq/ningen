from django.contrib import admin
from django.db import models
from django.forms import Textarea

from ningen.interview.models import Interview, Item, Person, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'gender', 'email')
    list_filter = ('gender', )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'vendor', 'name', 'slug')
    list_filter = ('vendor', )

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = '全称'


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('slug', 'person', 'title', 'company', 'education', 'create_on')
    list_filter = ('company', 'education', 'create_on')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols': 40})},
    }
