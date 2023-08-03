
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField
from stdimage import StdImageField
from archive.consts import *


class ArchiveDocument(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects = InheritanceManager()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    creator = models.CharField(max_length=50, blank="True")
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=True,
        blank = True,
    )


class Genre(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    name = models.CharField(max_length=200, blank = True)

class AudioRecording(ArchiveDocument):
    language = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank = True)
    recording_date = models.DateField(auto_now=True)
    audio_file = models.FileField(upload_to="sounds/", null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='genre')
    record_label = models.CharField(max_length=200, blank = True)



class GenreToRecord(models.Model):
    record = models.ForeignKey(
        AudioRecording, blank=False, null=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(
        Genre, blank=False, null=True, on_delete=models.CASCADE)

#class subGenre(Genre):
    #subgenre = models.CharField(max_length=200, blank = True)

class AssociatedImage(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    associated_doc = models.ForeignKey(
        ArchiveDocument, blank=False, null=False, on_delete=models.CASCADE)
    associated_doc1 = models.ForeignKey(
         GenreToRecord, blank=True, null=True, on_delete=models.CASCADE)
    associated_doc2 = models.ForeignKey(
         Genre, blank=True, null=True, on_delete=models.CASCADE)
    creator = models.CharField(max_length=200, blank=True)
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


class Artifact(ArchiveDocument):
    MAT_OTHER = 'other'
    MAT_PLASTIC = 'plastic'
    MAT_CERAMIC = 'ceramic'
    MAT_GLASS = 'glass'
    MAT_METAL = 'metal'

    MATERIAL_CHOICES = [(MAT_OTHER, "Other"),
                        (MAT_PLASTIC, "Plastic"),
                        (MAT_CERAMIC, "Ceramic"),
                        (MAT_GLASS, "Glass"),
                        (MAT_METAL,"Metal")]
    material = models.CharField(
        max_length=50, choices=MATERIAL_CHOICES, default=MAT_GLASS)
    model3d = models.URLField(max_length=500, blank="True")


class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    language = models.CharField(max_length=200)
    transcription = models.TextField(blank=True, null=False)
