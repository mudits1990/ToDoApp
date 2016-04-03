import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from .models import Tasks, Tags, TaskTagMapping
import json


def serialize_task_list_data(task_list):
    ret = [dict(taskName=task.task_name, taskId=task.task_id, bookmark=task.bookmark, done=task.done) for task in task_list]
    return ret


def index(request):
    context = RequestContext(request, {'request': request})
    return render_to_response("index.html", context_instance=context)


@csrf_exempt
def get_task_list(request):
    # GET request
    # get tags as well.
    try:
        task_list = Tasks.objects.all()
    except Exception as e:
        print e
    return HttpResponse(json.dumps(serialize_task_list_data(task_list)))


@csrf_exempt
def add_new_task(request):
    # POST request
    json_data = json.loads(request.body)
    new_task = None
    try:
        print json_data['taskName']
        new_task = Tasks(task_name=json_data['taskName'])
        new_task.save()
    except Exception as e:
        print e
    return HttpResponse(json.dumps({'taskId': new_task.task_id, 'taskName': new_task.task_name, 'bookmark': False, 'done': False}))


@csrf_exempt
def edit_task(request):
    # POST request
    json_data = json.loads(request.body)
    print json_data
    task = Tasks.objects.get(task_id=json_data['taskId'])
    print task
    task.task_name = json_data['taskName']
    task.bookmark = json_data['bookmark']
    task.done = json_data['done']
    task.save()
    return HttpResponse(json.dumps({'taskId': task.task_id, 'taskName': task.task_name, 'bookmark': task.bookmark, 'done': task.done}))


@csrf_exempt
def search_keyword(request):
    # GET request
    pass


