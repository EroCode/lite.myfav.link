from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer, LinkEntrySerializer, CategorySerializer, TagEntrySerializer

from api.models import LinkEntry, CategoryEntry, TagEntry

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LinkEntryViewSet(viewsets.ModelViewSet):
    queryset = LinkEntry.objects.all()
    serializer_class = LinkEntrySerializer

class CategoryEntryViewSet(viewsets.ModelViewSet):
    queryset = CategoryEntry.objects.all()
    serializer_class = CategorySerializer

class TagEntryViewSet(viewsets.ModelViewSet):
    queryset = TagEntry.objects.all()
    serializer_class = TagEntrySerializer