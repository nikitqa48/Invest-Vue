from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Profile)

class AdminProfile(admin.ModelAdmin):
    list_display = ['first_name', 'gender', 'username','email','phone']

@admin.register(Connect)

class ConnectAdmin(admin.ModelAdmin):
    list_display = ['name','surname','middle_name','email','phone','organisation','created']
    list_filter = ['organisation']
    search_fields = ['email','phone', 'organisation']

@admin.register(Region)

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_filter = ['name']

@admin.register(InformationForRegion)

class InformationForRegion(admin.ModelAdmin):
    list_display = ['region','power', 'water', 'gas', 'heat', 'water_out']

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

@admin.register(Brownfield)

class BrownfieldAdmin(admin.ModelAdmin):
    list_display = ['number', 'square', 'region', 'image']
    list_filter = ['region']
    search_fields = ['number', 'square']
    ordering = ['region']

@admin.register(Support)

class SupportAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Industry)

class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name']