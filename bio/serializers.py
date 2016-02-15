import logging
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import BasicAuthentication
from oauth2_provider.models import Application
from django.contrib.contenttypes.models import ContentType
from bio.models import Category, Template, Element, ModuleFunction, ModuleElement, ScriptElement, ModelScript, PipelineRecipe, Step, StepGroup, Ingredient, IngredientGroup, UserCodeGroup, Userfile
from itertools import chain


User = get_user_model()

class AuthSerializerMixin(object):
    def restore_object(self, attrs, instance=None):
        if attrs.get("username", None):
            attrs["username"] = attrs["username"].lower()
        if attrs.get("email", None):
            attrs["email"] = attrs["email"].lower()
        if attrs.get("password", None):
            attrs["password"] = make_password(base64.decodestring(attrs["password"]))
        return super(AuthSerializerMixin, self).restore_object(attrs, instance)

    def validate_password(self, attrs, source):
        if len(attrs[source]) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters")
        return attrs

class BaseModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(BaseModelSerializer, self).__init__(*args, **kwargs)
        self.fields['content_type'] = serializers.SerializerMethodField('get_content_type')

    def get_content_type(self, obj):
        return ContentType.objects.get_for_model(obj).pk

class UserSerializer(AuthSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')

class GroupSerializer(AuthSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

class RegisterSerializer(serializers.ModelSerializer):
    #client_id = serializers.SerializerMethodField('client_id')
    #client_secret = serializers.SerializerMethodField('client_secret')
    class Meta:
        model = User
        fields = ('username', 'email', 'password') #, 'client_id', 'client_secret'
        write_only_fields = ('email', 'password',)

    # def register_client_id(self, obj):
    #     return Application.objects.get(user=obj).client_id
    #
    # def register_client_secret(self, obj):
    #     return Application.objects.get(user=obj).client_secret

class LoginSerializer(AuthSerializerMixin, serializers.ModelSerializer):
    #client_id = serializers.SerializerMethodField('login_client_id')
    #client_secret = serializers.SerializerMethodField('login_client_secret')
    class Meta:
        model = User
        fields = ('username', 'password') # , 'client_id', 'client_secret'

    # def login_client_id(self, obj):
    #     return Application.objects.get(user=obj).client_id
    #
    # def login_client_secret(self, obj):
    #     return Application.objects.get(user=obj).client_secret

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_password(self, attrs, source):
        if len(attrs[source]) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters")
        return attrs

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('id', 'argument', 'default', 'template', 'owner')

class TemplateSerializer(serializers.ModelSerializer):
    elements = ElementSerializer(many=True, read_only=True)
    class Meta:
        model = Template
        fields = ('id', 'title', 'elements', 'category', 'owner')

class CategorySerializer(serializers.ModelSerializer):
    templates = TemplateSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'topic', 'templates', 'owner')

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptElement
        fields = ('id', 'name', 'description', 'inputformat', 'outputformat', 'parameters', 'datafile', 'created', 'scriptpath', 'modelscript', 'owner')

class ModelScriptSerializer(serializers.ModelSerializer):
    scripts = ScriptSerializer(many=True, read_only=True)
    class Meta:
        model = ModelScript
        fields = ('id', 'name', 'description', 'inputformat', 'outputformat', 'parameters', 'datafile', 'created', 'server', 'scriptpath', 'scripts', 'owner')#, 'model'

class ModuleElementSerializer(serializers.ModelSerializer):
    models = ModelScriptSerializer(many=True, read_only=True)
    class Meta:
        model = ModuleElement
        fields = ('id', 'name', 'description', 'scheduler', 'inputformat', 'outputformat', 'softwarecitation', 'softwarelink', 'parameters', 'datafile', 'created', 'memory', 'time', 'step', 'models', 'owner')#, 'function'

class ModuleSerializer(serializers.ModelSerializer):
    #modules = ModuleElementSerializer(many=True, read_only=True)
    class Meta:
        model = ModuleFunction
        fields = ('id', 'name', 'description', 'datafile', 'stepgroups', 'steps', 'created', 'owner')#, 'modules'

class PipelineRecipeSerializer(serializers.ModelSerializer):
    #ingredients = IngredientSerializer(many=True, read_only=False)
    #stepgroups = StepGroupSerializer(many=True, read_only=True)
    class Meta:
        model = PipelineRecipe
        fields = ('id', 'name', 'description', 'ingredients', 'stepgroups', 'equipment', 'resultpath', 'footnote', 'created', 'owner')#, 'inputpath'

class StepSerializer(serializers.ModelSerializer):
    modules = ModuleElementSerializer(many=True, read_only=True)
    class Meta:
        model = Step
        fields = ('id', 'title', 'scheduler', 'priority', 'follows', 'group', 'modules', 'owner')

class StepGroupSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    recipes = PipelineRecipeSerializer(many=True, read_only=True)
    functions = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = StepGroup
        fields = ('id', 'name', 'topic', 'steps', 'recipes', 'functions', 'owner')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'title', 'server', 'path', 'format', 'group', 'owner')

class IngredientGroupSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    recipes = PipelineRecipeSerializer(many=True, read_only=True)
    class Meta:
        model = IngredientGroup
        fields = ('id', 'name', 'topic', 'ingredients', 'recipes', 'owner') #

class UserCodeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCodeGroup
        fields = ('id', 'name')

class UserfileSerializer(serializers.ModelSerializer):
    models = ModelScriptSerializer(many=True, read_only=True)
    class Meta:
        model = Userfile
        fields = ('id', 'name','server', 'path', 'models', 'owner')
