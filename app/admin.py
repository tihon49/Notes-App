from django.contrib import admin
from .models import *


class ProductChooseInQuestion(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'value', 'note', 'completed']
    list_filter = ['name', 'note']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    list_filter = ['owner']
    inlines = [ProductChooseInQuestion]


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    pass