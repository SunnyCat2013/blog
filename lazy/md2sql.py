#!/usr/bin/python
# -*- coding:utf-8 -*-

import shutil
import sqlite3
import sys
import time
from datetime import datetime

sfile = 'db.sqlite3'

def md2sql(title, category, content, atc_id=-1, date_time=datetime.now()):
    # backup database file
    shutil.copyfile(sfile, sfile + '.bak')

    try:
        title = title.decode('utf-8')
        category = category.decode('utf-8')
        content = content.decode('utf-8')

        # insert into database
        connect = sqlite3.connect(sfile) # connect database

        if atc_id == -1:
            connect.execute( "INSERT INTO article_article(title, category, content, date_time) VALUES(?, ?, ?, ?)",(title, category, content, date_time))
        else:
            insert_string = ("INSERT INTO article_article(id, title, category, content, date_time) VALUES(?, ?, ?, ?)", (atc_id, title, category, content, date_time))

        connect.commit()
        connect.close()

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

    content = mfile.read()

    md2sql(title, category, content)


if __name__ == '__main__':
    prepare_file()
