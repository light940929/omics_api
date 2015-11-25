from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from bio.models import Category, Template, Element, ModuleFunction, ModuleElement, ScriptElement, Document , ModelScript, PipelineRecipe

# class MyModelAdminForm(forms.ModelForm):
#
#     datafile = models.FileField(upload_to='modules', help_text='File path', null=True, blank=True, editable=True)
#
#     class Meta(object):
#         model = ModuleFunction
#         fields = '__all__'
#
# class MyModelAdmin(admin.ModelAdmin):
#     form = MyModelAdminForm
#     def get_ordering(self, request):
#         if request.user.is_superuser == True:
#             return ['name', 'description', 'datafile', 'steps', 'created', 'owner']
#         else:
#             return ['name', 'description', 'steps', 'created', 'owner']


admin.site.register(Category)
admin.site.register(Template)
admin.site.register(Element)
admin.site.register(ModuleFunction)#, MyModelAdmin)
admin.site.register(ModuleElement)
admin.site.register(ModelScript)
admin.site.register(ScriptElement)
admin.site.register(Document)
admin.site.register(PipelineRecipe)
