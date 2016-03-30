import settings
import csv
from django.http import HttpResponse
from datetime import datetime
from django.template.context import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request, {'request': request})
    return render_to_response("index.html", context_instance=context)


def get_task_list(request):
    pass


def add_new_task(request):
    pass


def edit_task(request):
    pass


def search_keyword(request):
    pass

