
from readline import get_current_history_length
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField, DateField
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

    MATERIAL_CHOICES = [(MAT_OTHER, "Other"),
                        (MAT_PLASTIC, "Plastic"),
                        (MAT_CERAMIC, "Ceramic"),
                        (MAT_GLASS, "Glass")]
    material = models.CharField(
        max_length=50, choices=MATERIAL_CHOICES, default=MAT_GLASS)
    model3d = models.URLField(max_length=500, blank="True")


class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    language = models.CharField(max_length=200)
    transcription = models.TextField(blank=True, null=False)


#adding a new model for mugs
#inherits from ArchiveDocument
class StarbucksMug(ArchiveDocument):
    productionLocation = models.CharField(blank = True, max_length = 500) #where the mug was made
    displayedLocation = models.CharField(blank = True, max_length = 500) #what location the mug shows
    sizeOunces = models.IntegerField() #size in ounces
    #date = models.CharField(blank = True, max_length = 500)
    date = models.DateField(blank = True, auto_now=False, auto_now_add=False) #when it was made
    subject = models.CharField(max_length = 500) #what does the mug depict
    shapeDescription = models.TextField(null = False) #description of the mug shape
    
    #color options
    COL_RED = 'red'
    COL_ORANGE = 'orange'
    COL_YELLOW = 'yellow'
    COL_GREEN = 'green'
    COL_BLUE = 'blue'
    COL_PURPLE = 'purple'
    COL_BLACK = 'black'
    COL_WHITE = 'white'
    COL_GRAY = 'gray'
    COL_BROWN = 'brown'
    COL_MULTI = 'multi' #multiple colors
    COL_OTHER = 'other' 
    COLOR_CHOICES = [(COL_RED, "Red"), (COL_ORANGE, "Orange"), (COL_YELLOW, "Yellow"),
                    (COL_GREEN, "Green"), (COL_BLUE, "Blue"), (COL_PURPLE, "Purple"), 
                    (COL_BLACK, "Black"), (COL_WHITE, "White"), (COL_GRAY, "Gray"),
                    (COL_BROWN, "Brown"), (COL_MULTI, "Multi"), (COL_OTHER, "Other")]
    color = models.CharField(max_length=500, choices=COLOR_CHOICES, default=COL_MULTI)
    
    #season options
    SEA_SUMMER = 'summer'
    SEA_FALL = 'fall'
    SEA_WINTER = 'winter'
    SEA_SPRING = 'spring'
    SEA_NONE = 'none'
    SEA_CHOICES = [(SEA_SUMMER, "Summer"), (SEA_FALL, "Fall"), (SEA_WINTER, "Winter"), (SEA_SPRING, "Spring"), (SEA_NONE, "None")]
    season = models.CharField(max_length = 500, choices = SEA_CHOICES, default = SEA_NONE)
    
    holiday = models.CharField(blank = True, max_length = 500)
    text = models.TextField(blank = True, null = False) #text on the mug
    material = models.CharField(max_length = 500) #what the mug is made out of

    productLink = models.URLField(max_length = 500) #link to website with prodcut
    link3DModel = models.URLField(max_length = 500, blank = "True") #link to 3d model, if available