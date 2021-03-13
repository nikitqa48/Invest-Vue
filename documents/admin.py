from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import  forms

class SectionAdminForm(forms.ModelForm):
    text = forms.CharField(label ='Текст',widget=CKEditorUploadingWidget())
    class Meta:
        model = Section
        fields = '__all__'

@admin.register(Section)
class AdminSection(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    form = SectionAdminForm
    class Meta:
        fields = '__all__'

@admin.register(SubSection)
class AdminSubSection(admin.ModelAdmin):
    list_filter = ('section',)
    class Meta:
        fields = '__all__'


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'