from django.contrib import admin
from .models import *
from django import  forms


@admin.register(Connect)
class ConnectAdmin(admin.ModelAdmin):
    list_display = ['name','surname','middle_name','email','phone','organisation','created']
    list_filter = ['organisation']
    search_fields = ['email','phone', 'organisation']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_filter = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','body','publish','created','updated','id']
    list_filter = ('created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']


@admin.register(Greenfield)
class GreenfieldAdmin(admin.ModelAdmin):
    list_display = ['number','square','region','form','image']
    list_filter = ['region', 'form']
    search_fields = ['number','square']
    ordering = ['region']


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ['name', 'id']

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ['name', 'image', 'industry', 'sum', 'start', 'finish', 'body', 'now']

@admin.register(TypeProject)
class AdminTypeProject(admin.ModelAdmin):
    list_display = ['description']

@admin.register(PrivateForm)
class AdminFormProject(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name']

