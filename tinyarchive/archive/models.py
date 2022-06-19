from django.db import models
from stdimage import StdImageField
# Create your models here.

class Photograph(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=False)
    photo_image=StdImageField(
        upload_to="photographs/",
        variations={
            "thumbnail":{"width":300, "height":300}
            }
        )

