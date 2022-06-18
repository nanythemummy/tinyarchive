from django.db import models
from stdimage import StdImageField
# Create your models here.

class Photograph(models.Model):
    photo_image=StdImageField()