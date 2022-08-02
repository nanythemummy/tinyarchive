from django.contrib import admin
from archive.models import Photograph,Document,AssociatedImage, Artifact, StarbucksMug
# Register your models here.

class AssociatedImageInline(admin.StackedInline):
    model = AssociatedImage
    extra = 1
class DocumentAdmin(admin.ModelAdmin):
    inlines = [AssociatedImageInline]
admin.site.register(Photograph,DocumentAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Artifact,DocumentAdmin)
admin.site.register(StarbucksMug, DocumentAdmin)