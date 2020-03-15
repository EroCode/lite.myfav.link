from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import CategoryEntry, LinkEntry, TagEntry

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.HyperlinkedRelatedField(many=True, view_name='link-detail', read_only=True)

    class Meta:
        model = CategoryEntry
        fields = ('url', 'owner', 'name', 'links')
        

class TagEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagEntry
        fields = ('url', 'content_object')
        
class LinkEntrySerializer(serializers.HyperlinkedModelSerializer):
    #tags = serializers.StringRelatedField(many=True, read_only=True)
    tags = TagEntrySerializer(read_only=True, many=True)

    class Meta:
        model = LinkEntry
        fields = ('url', 'category_name', 'order', 'link', 'user', 'public_date', 'tags')