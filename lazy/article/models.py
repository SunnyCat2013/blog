from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    tags = models.ManyToManyField(Tag, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
