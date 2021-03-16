from django.contrib import admin
from .models import *
from django import  forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from parler.admin import TranslatableAdmin, TranslatableModelForm

class NewsAdminForm(TranslatableModelForm):
    body = forms.CharField(label ='Текст',widget=CKEditorUploadingWidget())
    class Meta:
        model = NewsTranslate
        fields = '__all__'

class SupportAdminForm(TranslatableModelForm):
    organisation = forms.CharField(label='Кто выдает меру поддержки', widget=CKEditorUploadingWidget())
    class Meta:
        model = SupportTranslate
        fields = '__all__'

class GreenfieldAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание участка" ,widget=CKEditorUploadingWidget())
    # nalog = forms.CharField(label='Налоговые льготы',widget=CKEditorUploadingWidget())
    class Meta:
        model = Greenfield
        fields = '__all__'

@admin.register(Connect)
class ConnectAdmin(admin.ModelAdmin):
    list_display = ['name','surname','middle_name','email','phone','organisation','created', 'check']
    list_filter = ['organisation', 'check']
    search_fields = ['email','phone', 'organisation']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_filter = ['name']


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title','body','publish','created','updated','id']
#     list_filter = ('created', 'publish')
#     search_fields = ('title', 'body')
#     form = NewsAdminForm
#     prepopulated_fields = {'slug': ('title',)}
#     date_hierarchy = 'publish'
#     ordering = ['publish']


# @admin.register(Greenfield)
# class GreenfieldAdmin(admin.ModelAdmin):
#     list_display = ['number','square','region','form','image']
#     list_filter = ['region', 'form']
#     search_fields = ['number','square']
#     ordering = ['region']
#     form = GreenfieldAdminForm


@admin.register(SupportTranslate)
class SupportAdmin(TranslatableAdmin):
    list_display = ['name']
    form = SupportAdminForm


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ['name', 'id']

@admin.register(ProjectTranslate)
class AdminProject(TranslatableAdmin):
    # list_display = ['name', 'image', 'industry', 'sum', 'start', 'finish', 'body', 'now', 'id']
    class Meta:
        model = ProjectTranslate
        fields = '__all__'

@admin.register(TypeProject)
class AdminTypeProject(admin.ModelAdmin):
    list_display = ['description']

@admin.register(PrivateForm)
class AdminPrivateForm(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ContactTranslate)
class AdminContact(TranslatableAdmin):
    list_display = ['name']
    class Meta:
        model = ContactTranslate
        fields = '__all__'

@admin.register(ProjectRequest)
class AdminProjectRequest(admin.ModelAdmin):
    list_display =['project']
    readonly_fields = ['project']

class AdminEvent(admin.ModelAdmin):
    list_display = ['organisation', 'name', 'second_name']


@admin.register(Greenfield)
class AdminTranslateGreenfield(admin.ModelAdmin):
    list_display = ['number','square','region','image']
    list_filter = ['region', 'form']
    search_fields = ['number','square']
    ordering = ['region']
    form = GreenfieldAdminForm
    
    class Meta:
        model = GreenfieldTranslate
        fields = '__all__'

@admin.register(NewsTranslate)
class NewsTranslateAdmin(TranslatableAdmin):
    list_filter = ('publish',)
    search_fields = ('title', 'body')
    form = NewsAdminForm
    # prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']

