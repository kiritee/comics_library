#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:16:32 2020

@author: konark
"""
test = 0
test_case = 1
log = 1

from conf import *
from comics_classes import *
import os
import re
import sys

if test == 1:
    root_path = codebase + "/Test_" + str(test_case)

if log == 1:
    log_file = open(codebase+"/log.tsv",'w',encoding="utf-8")
else:
    log_file = sys.stdout


print('\t'.join(['issue_id','path','collections','ext','name','series_name','volume','year','issue_no','confidence']), file = log_file)
issue_list = []
for paths,dirs,files in os.walk(root_path):
    for file in files:
        if file.startswith('._') or file =='.DS_Store':
            continue
        full_path = os.path.join(paths,file)
        
        rel_path = full_path.replace(root_path+'/','',1)
        collections = rel_path.split(sep='/')  
        collections.reverse()
        filename = collections.pop(0)
        i = filename.rfind('.')
        ext = filename[i+1:]
        
        if ext.lower() in ('cbr','cbz'):
            name = filename[:i]
            issue = Issue(full_path, name, ext, collections)
            issue.processName()
            issue_list.append(issue)
            print('\t'.join(str(e) for e in issue.__dict__.values()), file = log_file)
        

log_file.close()