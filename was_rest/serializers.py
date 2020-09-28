from rest_framework import serializers
from .models import *

class MediaFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('name', 'create_date')

class Stream_1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stream_1
        fields = ('pk', 'name', 'file_list')

class Stream_trajectory_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stream_trajectory
        fields = ('pk', 'name', 'file_list')