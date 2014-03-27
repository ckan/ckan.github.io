#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This script is used to import the old blog posts, into the new format.
It requires a path to a dump of the wordpress install so that it can locate
old blog posts and generate new files for them.
'''
import calendar
import os
import sys

if len(sys.argv) != 2:
    print 'Did you forget to say where the Wordpress dump is'
    sys.exit(1)

source = sys.argv[1]
print "Looking at {0}".format(source)

count = 0
for dirpath, _, _ in os.walk(source, topdown=True):
    if count == 1:
        break

    path = dirpath[len(source)+1:]
    if not path.startswith('20'):
        continue

    splitpath = path.split('/')
    if not len(splitpath) == 4:
        continue

    try:
        year = int(splitpath[0])
        month = int(splitpath[1])
        day = int(splitpath[2])
        slug = splitpath[3]
    except:
        continue

    count = count + 1

    date = "{0}-{1:02d}-{2:02d}".format(year,month,day)
    target = "_posts/blogposts/{0}-{1}.html".format(date,slug)

    title = "Blog title"

    front_matter = """
---
layout: post
categories: blogpost
date: {date}
title: ""
permalink: /{date}/{slug}
breadcrumbs:
    - Blog: /blog/
    - {year}: /blog/{year}
    - {month}: /blog/{year}/{month_num}
    - {day}: /blog/{year}/{month_num}/{day}
    - {title}: ''
---

CONTENT
    """.format(title=title, date=date.replace('-','/'),slug=slug,year=year,month=calendar.month_name[month],day=day, month_num=month)

    open(target,'w').write(front_matter.strip())