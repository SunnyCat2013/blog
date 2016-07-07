#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'lazy.settings'
import django
django.setup()
from django.conf import settings
import shutil
from article.models import Article
from article.models import Tag
from django.utils import timezone

sfile = 'db.sqlite3'
def md2sql(title, category, tags, content):
    # backup database file
    shutil.copyfile(sfile, sfile + '.bak')

    try:
        a = Article(title=title, category=category, content=content)
        a.save() # 执行下面之前要先保存
        for t in tags:
            try:
                tag = Tag.objects.get(tag__iexact=t)
            except:
                tag = Tag(tag=t)
                tag.save() # 执行下面之前要先保存

            a.tags.add(tag)
        a.save()
    except:
        print '--!Error: Failed write file into db.sqlite3!--'
        shutil.copyfile(sfile + '.bak', sfile)


def prepare_file():
    mfile = open(sys.argv[1], 'r')
    title = mfile.readline()
    if not title.startswith('#title:'):
        print '--!Error: title format is wrong!--'
        return
    else:
        title = title[7:-1]
        title = title.strip()

    category = mfile.readline()
    if not category.startswith('#category:'):
        print '--!Error: category format is wrong!--'
        return
    else:
        category = category[10:-1]
        category = category.strip()

    tags = mfile.readline()
    if not tags.startswith('#tags:'):
        print '--!Error: tags format is wrong!--'
        return
    else:
        tags = tags[6:-1]
        tags = tags.strip()
        tags = [one.strip() for one in tags.split(',')]

    content = mfile.read()

    md2sql(title, category, tags, content)


if __name__ == '__main__':
    prepare_file()
