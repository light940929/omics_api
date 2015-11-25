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
from django.conf import settings

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'category', views.CategoryViewSet)
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
#element_list = views.ElementViewSet.as_view({
    #'get': 'list',
    #'post': 'create'
#})
#element_detail = views.ElementViewSet.as_view({
    #'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
#})
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
# scriptElement_list = views.ScriptElementViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# scriptElement_detail = views.ScriptElementViewSet.as_view({
#     'get': 'retrieve',
#     #'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
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

MEDIA_ROOT = getattr(settings, "FILEBROWSER_MEDIA_ROOT", settings.MEDIA_ROOT)
MEDIA_URL = getattr(settings, "FILEBROWSER_MEDIA_URL", settings.MEDIA_URL)
DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

urlpatterns = [
    # API authentication
    url(r'^$', views.home, name='home'),
    url(r'^api/', include(router.urls)),
    #url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # Registration of new users
    #url(r'^register/$', views.Register.as_view(), name="register"),
    #url(r'^login/$', views.Login.as_view(), name="login"),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # the view to register our user with a third party token
    # the backend is the python social auth backend e.g. google
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^user/$', user_list, name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

    url(r'^group/$', group_list, name='group-list'),
    url(r'^group/(?P<pk>[0-9]+)/$', group_detail, name='group-detail'),

    url(r'^category/$', category_list, name='category-list'),
    url(r'^category/(?P<id>[0-9]+)/$', category_detail, name='category-detail'),

    url(r'^template/$', template_list, name='template-list'),
    url(r'^template/(?P<id>[0-9]+)/$', template_detail, name='template-detail'),

    #url(r'^template/(?P<id>[0-9]+)/element/$', element_list, name='element-list'),
    #url(r'^template/(?P<id>[0-9]+)/element/(?P<ck>[0-9]+)/$', element_detail, name='element-detail'),

    url(r'^pipeline/$', module_list, name='module-list'),
    url(r'^pipeline/(?P<id>[0-9]+)/$', module_detail, name='module-detail'),

    url(r'^module/$', moduleElement_list, name='moduleElement-list'),
    url(r'^module/(?P<id>[0-9]+)/$', moduleElement_detail, name='moduleElement-detail'),

    url(r'^modelscript/$', modelScript_list, name='modelScript-list'),
    url(r'^modelscript/(?P<id>[0-9]+)/$', modelScript_detail, name='modelScript-detail'),

    #url(r'^modelscript/(?P<id>[0-9]+)/script/$', scriptElement_list, name='scriptElement-list'),
    #url(r'^modelscript/(?P<id>[0-9]+)/script/(?P<ck>[0-9]+)/$', scriptElement_detail, name='scriptElement-detail'),

    url(r'^pipelinerecipe/$', recipe_list, name='recipe-list'),
    url(r'^pipelinerecipe/(?P<id>[0-9]+)/$', recipe_detail, name='recipe-detail'),

]

if settings.DEBUG:
        urlpatterns += patterns('',
            url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True,
            }),
            # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            #     'document_root': settings.STATIC_ROOT,
            #     'show_indexes': True,
            # }),
    )


