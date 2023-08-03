
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField
from stdimage import StdImageField
from archive.consts import *


class About_person(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects = InheritanceManager()
    name = models.CharField(max_length=50, blank="True")
    about_me_blurb = models.TextField(blank=True, null=False)
    favorite_song = models.CharField(max_length=50, blank="True")
    major = models.CharField(max_length=50, blank="True")
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=True,
        blank = True,
    )
