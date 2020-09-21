from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import  forms

class EventAdminForm(forms.ModelForm):
    description = forms.CharField(label ='описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Organisation)

class OrganisationAdmin(admin.ModelAdmin):
    model = Organisation

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    form = EventAdminForm
    
@admin.register(Winners)
class WinndersAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = ['name']