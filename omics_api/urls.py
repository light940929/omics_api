from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import url, include, patterns
from bio import views
from bio.models import Category, Template, Element
from rest_framework import routers, renderers
from bio.serializers import RegisterSerializer
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from filebrowser.sites import site
from django.views.generic import TemplateView

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
#router.register(r'category', views.CategoryViewSet)
# router.register(r'template', views.TemplateViewSet)
# router.register(r'element', views.ElementViewSet)
# router.register(r'module', views.ModuleViewSet)
# router.register(r'moduleElement', views.ModuleViewSet)
# router.register(r'model', views.ModelScriptViewSet)
# router.register(r'script', views.ScriptElementViewSet)


user_list = views.UserViewSet.as_view({
    'get': 'list'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

group_list = views.GroupViewSet.as_view({
    'get': 'list'
})

group_detail = views.GroupViewSet.as_view({
    'get': 'retrieve'
})

category_list = views.CategoryViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})

category_detail = views.CategoryViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

template_list = views.TemplateViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})

template_detail = views.TemplateViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

module_list = views.ModuleViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})

module_detail = views.ModuleViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

moduleElement_list = views.ModuleElementViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})

moduleElement_detail = views.ModuleElementViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

modelScript_list = views.ModelScriptViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

modelScript_detail = views.ModelScriptViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

recipe_list = views.PipelineRecipeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

recipe_detail = views.PipelineRecipeViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

step_list = views.StepViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

step_detail = views.StepViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

stepgroup_list = views.StepGroupViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

stepgroup_detail = views.StepGroupViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

ingredient_list = views.IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

ingredient_detail = views.IngredientViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

ingredientgroup_list = views.IngredientGroupViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

ingredientgroup_detail = views.IngredientGroupViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

userfile_list = views.UserfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

userfile_detail = views.UserfileViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


MEDIA_ROOT = getattr(settings, "FILEBROWSER_MEDIA_ROOT", settings.MEDIA_ROOT)
MEDIA_URL = getattr(settings, "FILEBROWSER_MEDIA_URL", settings.MEDIA_URL)
DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

urlpatterns = [
    # API authentication
    url(r'^$', TemplateView.as_view(template_name='home.html')), #views.home, name='home'
    url(r'^services/$', TemplateView.as_view(template_name='services.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^api/', include(router.urls)),
    #url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'^list/$', views.list, name='list'),
    #url(r'^register-by-token/(?P<backend>[^/]+)/$', views.Register.register_by_access_token),

    # Registration of new users
    #url(r'^register/$', views.Register.as_view(), name="register"),
    #url(r'^login/$', views.Login.as_view(), name="login"),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls')),

    # the view to register our user with a third party token
    # the backend is the python social auth backend e.g. google
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^categories/$', category_list, name='category-list'),
    url(r'^categories/(?P<id>[0-9]+)/$', category_detail, name='category-detail'),

    url(r'^templates/$', template_list, name='template-list'),
    url(r'^templates/(?P<id>[0-9]+)/$', template_detail, name='template-detail'),

    url(r'^pipelines/$', module_list, name='module-list'),
    url(r'^pipelines/(?P<id>[0-9]+)/$', module_detail, name='module-detail'),

    url(r'^modules/$', moduleElement_list, name='moduleElement-list'),
    url(r'^modules/(?P<id>[0-9]+)/$', moduleElement_detail, name='moduleElement-detail'),

    url(r'^modelscripts/$', modelScript_list, name='modelScript-list'),
    url(r'^modelscripts/(?P<id>[0-9]+)/$', modelScript_detail, name='modelScript-detail'),

    url(r'^pipelinerecipes/$', recipe_list, name='recipe-list'),
    url(r'^pipelinerecipes/(?P<id>[0-9]+)/$', recipe_detail, name='recipe-detail'),

    url(r'^steps/$', step_list, name='step-list'),
    url(r'^steps/(?P<id>[0-9]+)/$', step_detail, name='step-detail'),

    url(r'^stepgroups/$', stepgroup_list, name='stepgroup-list'),
    url(r'^stepgroups/(?P<id>[0-9]+)/$', stepgroup_detail, name='stepgroup-detail'),

    url(r'^ingredients/$', ingredient_list, name='ingredient-list'),
    url(r'^ingredients/(?P<id>[0-9]+)/$', ingredient_detail, name='ingredient-detail'),

    url(r'^ingredientgroups/$', ingredientgroup_list, name='ingredientgroup-list'),
    url(r'^ingredientgroups/(?P<id>[0-9]+)/$', ingredientgroup_detail, name='ingredientgroup-detail'),

    url(r'^userfiles/$', userfile_list, name='userfile-list'),
    url(r'^userfiles/(?P<id>[0-9]+)/$', userfile_detail, name='userfile-detail'),

]

if settings.DEBUG:
        urlpatterns += patterns('',
            url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True,
            })
    )


#urlpatterns = format_suffix_patterns(urlpatterns)
