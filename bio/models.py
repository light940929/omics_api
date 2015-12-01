from django import forms
from django.db import models
from oauth2_provider.models import Application
from oauth2_provider.models import AbstractApplication
from rest_framework.settings import api_settings
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError


class Category(models.Model):
    TOPIC = (
        ('DNA', 'DNA_SEQ'),
        ('RNA', 'RNA_SEQ'),
        ('CHIP', 'CHIP_SEQ'),
        ('OTHER', 'OTHER_TYPE'),
    )
    name = models.CharField(u'Name', max_length=20, help_text='Put the name of category')
    topic = models.CharField(max_length=10, choices=TOPIC, help_text='Select your topic')
    owner = models.ForeignKey(User, editable=False)

    def __unicode__(self):
        return self.name

class Template(models.Model):
    title = models.CharField(u'Title', max_length=50, help_text='Put the name of template')
    category = models.ForeignKey('Category', related_name='templates', help_text='Select the category')
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('category', 'title')

    def __unicode__(self):
        return self.title

class Element(models.Model):
    argument = models.CharField(u'Argument', max_length=20, help_text='Put the name of argument', db_index=True)
    default = models.CharField(u'Default', max_length=200, help_text='Put the defualt value such as PATH or VERSION', db_index=True, null=True, blank=True)
    template = models.ForeignKey('Template', related_name='elements', db_index=True)
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('template', 'argument')

    def __unicode__(self):
        return '%s= "%s",' % (self.argument.upper(), self.default)

class ModuleFunction(models.Model):
    def validate_file_extension(value):
        if value.file.content_type != 'text/plain':
           raise ValidationError(u'Error message')

    name = models.CharField(u'Name', max_length=30, help_text='Put your main pipeline name')
    description = models.CharField(max_length=200, help_text='Describe your pipeline')
    datafile = models.FileField(upload_to='modules', help_text='File path', null=True, blank=True, editable=False)#, validators=[validate_file_extension])
    steps = models.CharField(max_length=1000,help_text="Please steps by steps with the following format: <em>ModuleName1, ModuleName2&3, ModuleName4</em>.", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('name', 'owner')

    def __unicode__(self):
        return '%s.py' % (self.name)

class ModuleElement(models.Model):
    TOPIC = (
        ('SGE', 'Sun_Grid_Engine'),
        ('PBS', 'Protable_Batch_System'),
        ('LSF', 'Load_Sharing_Facility'),
        ('OTHER', 'OTHER TYPE'),
    )
    FILEFORMAT = (
        ('FASTQ', 'FASTQ FORMAT'),
        ('SAM', 'SAM FORMAT'),
        ('BAM', 'BAM FORMAT'),
        ('VCF', 'VCF FORMAT'),
        ('BED', 'BED FORMAT'),
        ('TXT', 'TXT FORMAT'),
        ('PDF', 'PDF FORMAT'),
        ('JPG', 'JPG FORMAT'),
        ('OTHER', 'OTHER FORMAT'),
    )
    name = models.CharField(u'Name', max_length=60, help_text='Put the name of module')
    description = models.CharField(max_length=200, help_text='Describe your module')
    scheduler = models.CharField('Scheduler', max_length=5, choices=TOPIC, help_text='Select your scheduler platform')
    inputformat = models.CharField(max_length=10, choices=FILEFORMAT, help_text='Select your input file format')
    outputformat = models.CharField(max_length=10, choices=FILEFORMAT, help_text='Select your output file format')
    softwarecitation = models.CharField(max_length=200, help_text='Put about software citation', null=True, blank=True)
    softwarelink = models.URLField(help_text='Put about software URL', null=True, blank=True) #verify_exists = True,
    #parameters = models.ManyToManyField('Element', help_text='Select the parameters you would need')
    parameters = models.CharField(max_length=300, help_text='Put your parameters such as BWA_RESULTS,  BWA_OPTIONS, BWA_VERSION')
    datafile = models.FileField(upload_to='moduleElements', help_text='File path', null=True, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    #function = models.ForeignKey('ModuleFunction', related_name='modules')
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('name', 'scheduler')#, 'function'

    def __unicode__(self):
        return '%s.py' % (self.name)

class ModelScript(models.Model):
    FILEFORMAT = (
        ('FASTQ', 'FASTQ FORMAT'),
        ('SAM', 'SAM FORMAT'),
        ('BAM', 'BAM FORMAT'),
        ('VCF', 'VCF FORMAT'),
        ('BED', 'BED FORMAT'),
        ('TXT', 'TXT FORMAT'),
        ('PDF', 'PDF FORMAT'),
        ('JPG', 'JPG FORMAT'),
        ('OTHER', 'OTHER FORMAT'),
    )
    name = models.CharField(u'Name', max_length=60, help_text='Put the name of model')
    description = models.CharField(max_length=200, help_text='Describe your model', null=True, blank=True)
    inputformat = models.CharField(max_length=10, choices=FILEFORMAT, help_text='Select your input file format')
    outputformat = models.CharField(max_length=10, choices=FILEFORMAT, help_text='Select your output file format')
    #parameters = models.ManyToManyField('Element', help_text='Select the parameters you would need', null=True, blank=True)
    parameters = models.CharField(max_length=300, help_text='Put your parameters such as BWA_RESULTS,  BWA_OPTIONS, BWA_VERSION')
    datafile = models.FileField(upload_to='scripts', help_text='File path', null=True, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    scriptpath = models.CharField(max_length=300, help_text='Put file path with the following format: <em>PATH_TO/Script, ServerName</em>.')
    model = models.ForeignKey('ModuleElement', related_name='models', help_text='Put your module id', default = '0', editable=False)
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('name', 'scriptpath')#, 'model'

    def __unicode__(self):
        return self.name

class ScriptElement(models.Model):
    FILEFORMAT = (
            ('FASTQ', 'FASTQ FORMAT'),
            ('SAM', 'SAM FORMAT'),
            ('BAM', 'BAM FORMAT'),
            ('VCF', 'VCF FORMAT'),
            ('BED', 'BED FORMAT'),
            ('TXT', 'TXT FORMAT'),
            ('PDF', 'PDF FORMAT'),
            ('JPG', 'JPG FORMAT'),
            ('OTHER', 'OTHER FORMAT'),
    )
    name = models.CharField(u'Name', max_length=60, help_text='Put the name of script element')
    description = models.CharField(max_length=200, help_text='Describe your script element')
    inputformat = models.CharField(max_length=10, choices=FILEFORMAT, help_text='Select your input file format', null=True, blank=True)
    outputformat = models.CharField(max_length=10, choices=FILEFORMAT, help_text='Select your output file format', null=True, blank=True)
    #parameters = models.ManyToManyField('Element', help_text='Select the parameters you would need')
    parameters = models.CharField(max_length=300, help_text='Put your parameters such as BWA_RESULTS,  BWA_OPTIONS, BWA_VERSION', null=True, blank=True)
    datafile = models.FileField(upload_to='scriptElements', help_text='File path', null=True, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    scriptpath = models.CharField(max_length=300, help_text='Put file path with the following format: <em>PATH_TO/Script, ServerName</em>.')
    modelscript = models.ForeignKey('ModelScript', related_name='scripts', help_text='Put your model id')
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('name', 'modelscript')

    def __unicode__(self):
        return self.name

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class PipelineRecipe(models.Model):
    name = models.CharField(u'Name', max_length=30, help_text='Put your special menu name')
    description = models.CharField(max_length=200, help_text='Describe your ingredients and directions')
    ingredientname = models.CharField(max_length=500, help_text="Please put the name of ingredients with the following format: <em>cbd1, cbd2, cbd3</em>.")
    steps = models.CharField(max_length=1000,help_text="Please steps by steps with the following format: <em>ModuleName1, ModuleName2&3, ModuleName4</em>.", null=True, blank=True)
    equipment = models.CharField(max_length=200, help_text="If the process need special version or library, please note with the following format: <em>PYTHON_VERSION: 2.7.9</em>.", null=True, blank=True)
    inputpath = models.CharField(max_length=400, help_text="Please put the path of raw data")
    resultpath = models.CharField(max_length=400, help_text="Please put the path of output results")
    footnote = models.CharField(max_length=500, help_text="If you need special database or reference, please give information with the following format: <em>MULTICOV_EXONFILE: /refgenomes/mm9/exons.bed</em>. ", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, editable=False)

    class Meta:
        unique_together = ('name', 'owner')

    def __unicode__(self):
        return self.name

# class Upload(models.Model):
#     pic = models.ImageField("Image", upload_to="images")
#     upload_date=models.DateTimeField(auto_now_add =True)
#
# # FileUpload form class.
# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Upload
#         fields = "__all__"

# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, password, groups, is_active, **extra_fields):
#         """
#         Creates and saves a User with the given username, email and password.
#         """
#         user = self.model(username=username, email=email, groups=groups,
#                           is_active=True, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, email=None, password=None, groups=None, **extra_fields):
#         return self._create_user(username, email, password, groups, False, **extra_fields)
#
#     def create_superuser(self, username, email, password, groups, **extra_fields):
#         return self._create_user(username, email, password, groups, True, **extra_fields)
#

# class Application(AbstractApplication):
#     """
#     Custom Application model which adds description field
#     """
#     description = models.TextField(blank=True)
