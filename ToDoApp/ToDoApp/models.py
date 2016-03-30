from django.db import models


class Task(models.Model):
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=200)


class Tag(models.Model):
    tag_id = models.IntegerField()
    tag_name = models.CharField(max_length=200)


class TaskTagMapping(models.Model):
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE)

