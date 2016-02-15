from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework.exceptions import APIException
from rest_framework import generics, status, viewsets, permissions, renderers, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import list_route, detail_route
from permissions import IsOwnerOrReadOnly
from permissions import IsAuthenticatedOrCreate
from bio.serializers import RegisterSerializer, UserSerializer, GroupSerializer, LoginSerializer, PasswordSerializer, CategorySerializer, TemplateSerializer, ElementSerializer, ModuleSerializer, ModuleElementSerializer, ScriptSerializer, ModelScriptSerializer, PipelineRecipeSerializer, StepSerializer, StepGroupSerializer, IngredientSerializer, IngredientGroupSerializer, UserCodeGroupSerializer, UserfileSerializer
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from tools import get_access_token
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from social.actions import do_complete
from social.apps.django_app.utils import strategy
from social.apps.django_app.views import _do_login
from bio.models import Category, Template, Element, ModuleFunction, ModuleElement, ScriptElement, ModelScript, PipelineRecipe, Step, StepGroup, Ingredient, IngredientGroup, UserCodeGroup, Userfile
from itertools import chain
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponseRedirect
from django.conf import settings


User = get_user_model()

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
   context = RequestContext(request,
                           {'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #parser_classes = (YAMLParser,)
    #renderer_classes = (YAMLRenderer,)
    #permission_classes = (IsAuthenticatedOrCreate,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #parser_classes = (YAMLParser,)
    #renderer_classes = (YAMLRenderer,)
    #permission_classes = (IsOwnerOrReadOnly,)


class Register(generics.CreateAPIView):
    """
    API endpoint that allows users to sign up and then be edited.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

    # When we send a third party access token to that view
    # as a GET request with access_token parameter
    @psa('social:complete')
    def register_by_access_token(request, backend):

        token = request.GET.get('access_token')
        # here comes the magic
        user = request.backend.do_auth(token)
        if user:
            login(request, user)
            # that function will return our own
            # OAuth2 token as JSON
            # Normally, we wouldn't necessarily return a new token, but you get the idea
            return get_access_token(user)
        else:
            # If there was an error... you decide what you do here
            return HttpResponse("error")


class Login(generics.ListAPIView):
    """
    API endpoint that allows users to login and then to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = (BasicAuthentication,)
    # def get_queryset(self):
    #     return [self.request.user]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Category.objects.filter(owner=user)

class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    ordering_fields = ('category', 'owner')
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Template.objects.filter(owner=user)

class ElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    ordering_fields = ('template', 'owner')
    lookup_field = ('id')

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        #user = self.request.user
        template = self.kwargs['id']
        #element = self.kwargs['ck']
        return Element.objects.filter(template=template) #owner=user,, id=element

class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ModuleFunction.objects.all()
    serializer_class = ModuleSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        #datafile = self.request.data.get('datafile')
        #uploaded_file = serializers.FileField(use_url=True)
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    # def get_queryset(self):
    #     user = self.request.user
    #     # if user.is_superuser == True:
    #     #    adminfile = self.kwargs['datafile']
    #     #    return ModuleFunction.objects.filter(owner=user, datafile=)
    #     return ModuleFunction.objects.filter(owner=user)


class ModuleElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ModuleElement.objects.all()
    serializer_class = ModuleElementSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    ordering_fields = ('name', 'owner')
    lookup_field = 'id'
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     user = self.request.user
    #     #module = self.kwargs['id']
    #     return ModuleElement.objects.filter(owner=user)#, function=module

class ModelScriptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ModelScript.objects.all()
    serializer_class = ModelScriptSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)

   # def get_queryset(self):
   #     user = self.request.user
   #     return ModelScript.objects.filter(owner=user)

class ScriptElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ScriptElement.objects.all()
    serializer_class = ScriptSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    #ordering_fields = ('name', 'owner')
    lookup_field = 'id'
    from bio.forms import DocumentForm

    form = DocumentForm()
    def perform_create(self, serializer):
        user = self.request.user
        #datapath = self.kwargs['datapath']
        serializer.save(owner=self.request.user)#, datafile=datapath)

    def get_queryset(self):
        user = self.request.user
        model = self.kwargs['id']
        return ScriptElement.objects.filter(owner=user, modelscript=model)

class PipelineRecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = PipelineRecipe.objects.all()
    serializer_class = PipelineRecipeSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    def get_queryset(self):
        user = self.request.user
        return PipelineRecipe.objects.filter(owner=user)


class StepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    def get_queryset(self):
        user = self.request.user
        return Step.objects.filter(owner=user)


class StepGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = StepGroup.objects.all()
    serializer_class = StepGroupSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    def get_queryset(self):
        user = self.request.user
        return StepGroup.objects.filter(owner=user)


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    def get_queryset(self):
        user = self.request.user
        return Ingredient.objects.filter(owner=user)


class IngredientGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = IngredientGroup.objects.all()
    serializer_class = IngredientGroupSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    def get_queryset(self):
        user = self.request.user
        return IngredientGroup.objects.filter(owner=user)


class UserCodeGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserCodeGroup.objects.all()
    serializer_class = UserCodeGroupSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'


class UserfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Userfile.objects.all()
    serializer_class = UserfileSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=self.request.user)#, uploaded_file=datafile)

    def get_queryset(self):
        user = self.request.user
        return Userfile.objects.filter(owner=user)


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from bio.models import Document
from bio.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('bio.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
