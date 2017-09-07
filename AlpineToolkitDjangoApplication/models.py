####################################################################################################
#
# Alpine Toolkit - 
# Copyright (C) 2017 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

import logging

import os

# from datetime import datetime

from django.contrib.auth.models import User
# from django.contrib.postgres.fields import JSONField
# from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

# from django.contrib.gis.db import models
from django.contrib.gis.db.models import (Model,
                                          ForeignKey,
                                          IntegerField,
                                          CharField, TextField,
                                          DateTimeField,
                                          PointField,
                                          ManyToManyField)

from filer import settings as filer_settings
from filer.fields.file import FilerFileField
# from filer.fields.image import FilerImageField
from filer.models.filemodels import File

####################################################################################################

from .settings import LANGUAGES

####################################################################################################

_module_loger = logging.Logger(__name__)

####################################################################################################

class Profile(models.Model):

    """This class defines a user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(verbose_name=_('language'), max_length=4,
                                choices=LANGUAGES, default='fr',
                                blank=True, null=True)

    ##############################################

    def __str__(self):
        return "{0.user}".format(self)

####################################################################################################

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

####################################################################################################

class JsonFile(File):

    _logger = _module_loger.getChild('JsonFile')

    author = CharField(_('author'), max_length=255, null=True, blank=True)

    version = IntegerField(_('version'), null=True, blank=False)

    date = DateTimeField(_('date'), null=True, blank=False)

    # must_always_publish_author_credit = models.BooleanField(_('must always publish author credit'), default=False)
    # must_always_publish_copyright = models.BooleanField(_('must always publish copyright'), default=False)

    class Meta(object):
        app_label = 'filer'
        verbose_name = _('json file')
        verbose_name_plural = _('json files')
        default_manager_name = 'objects'

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        print("matches_file_type", cls, iname, ifile, request)
        cls._logger.info("matches_file_type", iname, ifile)
        # the extensions we'll recognise for this file type
        filename_extensions = ['.json']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions

class FilerJsonFileField(FilerFileField):
    default_model_class = JsonFile

filer_settings.FILER_FILE_MODELS = [JsonFile] + list(filer_settings.FILER_FILE_MODELS)
print(filer_settings.FILER_FILE_MODELS)

####################################################################################################

class Document(models.Model):

    document = FilerJsonFileField(null=True,
                                  blank=True,
    )

    ##############################################

    def  __str__(self):

        return "{0.description} - {0.name}".format(self.document)
