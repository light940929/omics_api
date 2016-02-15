from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from bio.models import Category, Template, Element, ModuleFunction, ModuleElement, ScriptElement, Document, ModelScript, PipelineRecipe, Step, StepGroup, Ingredient, IngredientGroup, UserCodeGroup, Userfile


admin.site.register(Category)
admin.site.register(Template)
admin.site.register(Element)
admin.site.register(ModuleFunction)#, MyModelAdmin)
admin.site.register(ModuleElement)
admin.site.register(ModelScript)
admin.site.register(ScriptElement)
admin.site.register(Document)
admin.site.register(PipelineRecipe)
admin.site.register(Step)
admin.site.register(StepGroup)
admin.site.register(Ingredient)
admin.site.register(IngredientGroup)
admin.site.register(UserCodeGroup)
admin.site.register(Userfile)
