from re import template
from django.shortcuts import render
from django.http import HttpResponse
from archive.models import ArchiveDocument
from .models import Exhibit


def exhibit_index(request):
    context = {}
    exhibits = []
    try:
        allexhibits = Exhibit.objects.all()
        for exhibit in allexhibits:
            exhibits.append(
                {
                    "id": exhibit.id,
                    "name": exhibit.title,
                    "snippet": exhibit.short_description,
                }
            )
    except Exhibit.DoesNotExist as e:
        # This exception gets suppressed and we pass an empty exhibits variable to the template in the context.
        # the template will know what to do with it. All other exceptions get raised.
        print(e)
    context["exhibits"] = exhibits
    return render(request, "exhibit/index.html", context)


def exhibit_detail(request, exhibit_id):
    context = {}
    exhibit = Exhibit.objects.get(id=exhibit_id)
    archive_items = exhibit.items_in_exhibit.all()
    context = {
        "title": exhibit.title,
        "exhibit_text": exhibit.exhibit_text,
        "exhibit_items": [],
    }
    for item in archive_items:
        exhibit_item = {
            "id": item.id,
            "name":item.name,
            "description": item.description,
            "image": item.photo_image.thumbnail,
        }
        context["exhibit_items"].append(exhibit_item)
    return render(request,"exhibit/detail.html", context)
