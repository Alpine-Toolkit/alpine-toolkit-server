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

from rest_framework import serializers

####################################################################################################

from .models import (
    Document,
)

####################################################################################################

# class DocumentSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Document
#         fields = ('document',)

class DocumentSerializer(serializers.Serializer):

    name = serializers.CharField(source='document.name')
    author = serializers.CharField(source='document.author', max_length=255)
    version = serializers.IntegerField(source='document.version')
    date = serializers.DateTimeField(source='document.date')
    description = serializers.CharField(source='document.description')
    url = serializers.URLField(source='document.url', max_length=200, min_length=None, allow_blank=False)
    size = serializers.IntegerField(source='document.size')
