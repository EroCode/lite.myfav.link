from django.contrib.auth.models import User
from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from api.models import CategoryEntry, LinkEntry

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.HyperlinkedRelatedField(many=True, view_name='link-detail', read_only=True)

    class Meta:
        model = CategoryEntry
        fields = ('url', 'owner', 'name', 'links')
        

class LinkEntrySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = LinkEntry
        fields = ('url', 'category_name', 'order', 'link', 'user', 'public_date', 'tags')