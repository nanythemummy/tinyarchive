from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import ArchiveDocument, Photograph
from model_utils.managers import InheritanceManager
from .consts import Choices


def index(request):
    context = {}
    items_to_list = []
    """ Tries to get any photographs. If there aren't any, list won't 
        be filled and the template will receive a blank list.
    """
    try:
        archive_items = ArchiveDocument.objects.all()
        for item in archive_items:
            print(item.photo_image.thumbnail)
            archive_item_info = {
                "id": item.id,
                "thumbnail": item.photo_image.thumbnail,
                "name": item.name,
                "description": item.description,
            }

            items_to_list.append(archive_item_info)
    except Exception as e:
        print(e)
    context["archive_items"] = items_to_list
    return render(request, "archive/index.html", context)


def item_detail(request, item_id):
    context = {}
    template_to_render = ""
    try:
        archive_item = ArchiveDocument.objects.get_subclass(id=item_id)
        context["item"] = {
            "name": archive_item.name,
            "picture": archive_item.photo_image,
            "description": archive_item.description,
        }
        if isinstance(archive_item, Photograph):
            template_to_render = "archive/photo.html"
            # Photo type is the user-readable version of the Photo Type, as described in Consts.
            context["item"]["photo_type"] = Choices.PHOTO_TYPE_CHOICES[
                archive_item.photo_type
            ]
            template_to_render = "archive/item_photograph.html"
        else:
            context["item"]["transcription"] = archive_item.transcription
            context["item"]["language"] = archive_item.language
            template_to_render = "archive/item_document.html"

    except Exception as e:
        print(e)
        raise e
    print(template_to_render)
    return render(request, template_to_render, context)
