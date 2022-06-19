from django.shortcuts import render
from django.http import HttpResponse
from .models import Photograph


def index(request):
    context = {}
    items_to_list = []
    """ Tries to get any photographs. If there aren't any, list won't 
        be filled and the template will receive a blank list.
    """
    try:
        archive_items = Photograph.objects.all()
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
    try:
        archive_item = Photograph.objects.get(id=item_id)
        context["item"] = {
            "name": archive_item.name,
            "picture": archive_item.photo_image,
            "description": archive_item.description,
        }

    except Exception as e:
        print(e)
    return render(request, "archive/item_detail.html", context)
