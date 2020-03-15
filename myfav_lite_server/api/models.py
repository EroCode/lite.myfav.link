from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

# Link likes a track, belongs a album(CategoryEntry)
class CategoryEntry(models.Model):
    owner = models.ForeignKey(
        User, 
        related_name='user', 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    name = models.CharField(max_length=255, blank=False)
    links = models.ManyToManyField('LinkEntry', blank=True)

class TagEntry(TaggedItemBase):
    #name = models.CharField(max_length=25, blank=False)
    content_object = models.CharField(max_length=25, blank=False)

class LinkEntry(models.Model):
    category_name = models.ForeignKey(
        CategoryEntry, 
        related_name="category", 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    order = models.IntegerField()
    link = models.URLField(max_length=2550, blank=False)
    user = models.ForeignKey(
        User,
        #related_name='user',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    public_date = models.DateTimeField('date published')
    #tags = models.ManyToManyField('TagEntry')
    tags = TaggableManager(through=TagEntry, blank=True)