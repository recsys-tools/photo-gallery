from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from gallery_with_django.view_handler import get_context_gallery, delete
from gallery_with_django.settings import IMG_DATA_DIR


def index(request, page_id=None):
    context = get_context_gallery(IMG_DATA_DIR, page_id)

    return render(request, 'gallery.html', context)


def select_images(request, page_id=None):
    context = get_context_gallery(IMG_DATA_DIR, page_id)
    return render(request, 'delete_image.html', context)


@csrf_exempt
def delete_images(request):
    files = json.loads(request.body)
    delete(IMG_DATA_DIR, files)
    return HttpResponse()
