#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Test Filesystem
"""


from conf import *
import os

#Create testing space with exact same filestructure

for i in range(1,4):
    test_path = codebase + "/Test_"+str(i)
    for path,dirs,files in os.walk(root_path):
        new_path=path.replace(root_path, test_path)
        os.makedirs(new_path, exist_ok=True)
        os.chdir(new_path)
        for file in files:
            f = open(file,'ab')
            f.close()
    