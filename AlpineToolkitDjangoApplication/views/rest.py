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

from rest_framework import viewsets, permissions, generics
import django_filters
import rest_framework_filters

####################################################################################################

from ..serializers import (
    DocumentSerializer,
)

from ..models import (
    Document,
)

####################################################################################################

class DocumentFilter(rest_framework_filters.FilterSet): # django_filters.rest_framework.FilterSet

    class Meta:
        model = Document
        fields = {
            # cf. https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups
            'document__name' : ['exact', 'icontains'],
            'document__description' : ['icontains'],
            'document__version' : ['exact', 'gt'],
            # http://127.0.0.1:8000/api/documents/?document__date__gt=2017-04-21T18:28:11Z
            'document__date' : ['gt'],
        }

####################################################################################################

class DocumentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_backends = (rest_framework_filters.backends.DjangoFilterBackend,)
    filter_class = DocumentFilter
