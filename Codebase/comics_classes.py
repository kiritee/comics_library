#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:36:57 2020

@author: konark
"""
from conf import root_path
from ParseName import *
import re
import datetime



class Issue:
    issue_count = 0
    
    def get_issue_count():
        return Issue.issue_count
    
    def __init__(self, path = root_path, name='', ext='', collections=[], \
                 series_name = '', volume = -1, year = -1, issue_no =-1,confidence = 0):
        Issue.issue_count += 1        
        self.issue_id = Issue.issue_count
        self.path = path
        self.collections = collections
        self.ext = ext
        self.name = name
        self.series_name = series_name
        self.volume = volume
        self.year = year
        self.issue_no = issue_no
        self.confidence = confidence
        
    def _hygiene_(self):
        self.name = processSpaceUnderscoreHyphen(self.name)
        self.name = processStartingNumbers(self.name)
        '''
        a = re.search('[a-zA-Z]',self.name)
        if a is not None:
            firstchar = a.start()
            self.name = self.name[firstchar:]
        '''
    
    def _findYear_(self):
        self.year, self.name = findYear(self.name)
        
    def _findIssueNo_(self):
        self.issue_no, self.series_name, self.issue_confidence = findIssueNo(self.name)
        
    def _findVol_(self):
        volume, series_name  = findVol(self.series_name)
#        if volume == -1:
#            volume, series_name  = findVol(self.collections[0])
        self.series_name = series_name
        self.volume = volume
     

        
    def processName(self):   
        self._hygiene_()
        self._findYear_()
        self._findIssueNo_()
        self._findVol_()
        

  
    @property 
    def name(self):
        return self._name_
        
    @property 
    def ext(self):
        return self._ext_
    
    @property 
    def path(self):
        return self._path_
        
    @property 
    def collections(self):
        return self._collections_
    
    
    @name.setter 
    def name(self,value):
        self._name_ = value

    @ext.setter 
    def ext(self,value):
        self._ext_ = value

    @path.setter 
    def path(self,value):
        self._path_ = value

    @collections.setter 
    def collections(self,value):
        self._collections_ = value
   
    
        