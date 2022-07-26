
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField
from stdimage import StdImageField
from archive.consts import *


class ArchiveDocument(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects=InheritanceManager()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
    )

class AssociatedImage(models.Model):
 
    name = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    associated_doc = models.ForeignKey(ArchiveDocument,blank = False,null=False,on_delete=models.CASCADE)
    creator = models.CharField(max_length=200)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=False
    )
    def __str__(self):
        return(self.photo_image.url)
    

class Photograph(ArchiveDocument):
    photo_type = models.CharField(
        max_length=20,
        choices=list(
            Choices.PHOTO_TYPE_CHOICES.items()
        ),  # defining the constant as a dictionary for easy lookup in views.
    )


class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    language = models.CharField(max_length=200)
    transcription = models.TextField(blank=True, null=False)
