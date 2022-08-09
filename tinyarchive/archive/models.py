
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


class AssociatedImage(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    associated_doc = models.ForeignKey(
        ArchiveDocument, blank=False, null=False, on_delete=models.CASCADE)
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
    title = models.CharField(max_length=500, default="N/A")
    language = models.CharField(max_length=200)
    contributor_names = models.CharField(max_length=500, default="N/A")
    location_published = models.CharField(max_length=500, default="N/A")
    subject_headings = models.TextField(blank=True, null=False)
    summary = models.TextField(blank=True, null=False)
    GENRE_WEB = 'website'
    GENRE_OTHER = 'other'
    GENRE_CHOICES = [(GENRE_WEB, "Website"),
                     (GENRE_OTHER, "Other")]
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default=GENRE_WEB)
    FORM_ELECTRONIC = "electronic"
    FORM_OTHER = 'other'
    FORM_CHOICES = [(FORM_ELECTRONIC, "Electronic"),
                     (FORM_OTHER, "Other")]
    form = models.CharField(max_length=50, choices=FORM_CHOICES, default=FORM_ELECTRONIC)
    ONLINE_FORMAT_WEB = "web page"
    ONLINE_FORMAT_OTHER = "other"
    ONLINE_FORMAT_CHOICES = [(ONLINE_FORMAT_WEB, "Web Page"),
                             (ONLINE_FORMAT_OTHER, "Other")]
    online_format = models.CharField(max_length=50, choices=ONLINE_FORMAT_CHOICES, default=ONLINE_FORMAT_WEB)
    source_URL = models.TextField(blank=True, null=False)
    PDF = models.FileField(upload_to="uploads/", default="N/A")
