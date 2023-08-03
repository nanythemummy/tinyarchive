from django.shortcuts import render
from django.http import HttpResponse

# This is just the view for the static about.
def about_us(request):
    context = {}
    #return render(request, "about_us/about_us.html", {})
    return render(request, "about_us.html", {})