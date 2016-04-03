from django.db import models


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True, )
    task_name = models.CharField(max_length=200)
    bookmark = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.task_id)


class Tags(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.tag_id)


class TaskTagMapping(models.Model):
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)


