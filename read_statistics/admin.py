from django.contrib import admin
from .models import ReadNum, ReadDeteil


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')


@admin.register(ReadDeteil)
class ReadDeteilAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')
