#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:34:04 2020

@author: konark
"""

import re
import datetime

def processSpaceUnderscoreHyphen(name):
    processedName = name.replace('_',' ').replace('-',' - ').replace('#',' #').replace('[','(').replace(']',')') 
    return ' '.join(processedName.split())

def processStartingNumbers(name):
    words = name.split()
    if words != [] and re.match(r'^[0-9]+[a-z]?$',words[0]):
        return ' '.join(words[1:])
    else:
        return name
    
def cleanup(name):
    return ' '.join(processStartNonalpha(name).split())


def processStartNonalpha(name):
    processedName = name
    words = name.split()
    if words !=[] and words[0] != '52':
        while words != []:
            word = words.pop(0)
            a = re.search(r'[a-zA-z]',word)
            if a is not None:
                processedName = ' '.join([word]+words)
                break
    return processedName

def findYear(name):
    year = -1
    processedName = name
    m = re.findall(r'\([1-2]\d\d\d',name)
    if len(m)>0:
        m.reverse()
        num = int(m[0][1:])
        if num >= 1900 and num <= (datetime.datetime.now()).year:
            year = num
            processedName = name[:name.rfind(m[0])].strip()
    return year, cleanup(processedName)

def findIssueNo(name):
    issue_no = 1
    processedName = name
    confidence = 0
    words = name.split()
    words.reverse()
    while words != []:
        word = words.pop(0)
        
        #search for #XX type
        if re.match(r'^\#[0-9]+[a-z]?$',word):
            issue_no = int(re.sub(r'[\#a-z]','',word))
            words.reverse()
            processedName = ' '.join(words)
            confidence = 100
            break
        
        #search for n (of N) 
        if re.match(r'^\( *of',word):
            word  = words.pop(0)
            issue_no = int(re.sub(r'[\#a-z]','',word))
            words.reverse()
            processedName = ' '.join(words)
            confidence = 100
            break
        
        #search for n
        if re.match(r'^[0-9]+[a-z]?$',word):
            issue_no = int(re.sub(r'[\#a-z]','',word))
            words.reverse()
            processedName = ' '.join(words)
            confidence = 75
            break            
        
    return issue_no,cleanup(processedName), confidence

def findVol(name):
    vol = -1
    processedName = name
#    confidence = 0
    
    words = name.split()
    words.reverse()
    while words != []:
        word = words.pop(0)        
        m = re.findall(r'v\d+',word.lower())
        if len(m)>0:
            m.reverse()
            vol = int(m[0][1:])
            i = word.lower().rfind(m[0])  
            words.reverse()
            processedName = ' '.join(words + [word[:i]])
    return vol, cleanup(processedName)
    

'''
year,name = findYear(processStartingNumbers(processSpaceUnderscoreHyphen(input())))
issue, name, issue_confidence = findIssueNo(name)
vol, name = findVol(name)
print(year, name, vol, issue)


215a_Day of Vengeance - Infinite Crisis Special 34 (of 36) (2006) (Shazam-DCP)
001_Green Lantern #46-Parallax Saga
Catwoman 011 (2002-11) (DeadmanWade-DCP) (digital)
Batgirl v02 - Knightfall Descends (2013) (digital) (Son of Ultron-Empire) 2
160_Aquaman v5 036 (2005) (Sinestro-SSS)

Superman, 1985 - 09 - 00 ( #413) (digital) (OkC.O.M.P.U.T.O. - Novus - HD)
'''