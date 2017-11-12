# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 08:39:05 2017

@author: JoJo
"""

import random


def onepoint(p1,p2):
  parentlength = length(p1) - 1
  #create children 1 and 2
  c1 = []
  c2 = []
  cuttpoint = random.randint

  
  
  return c1,c2

def initialize():
    p1=[1,2,3,4,5,6,7,8,9]
    p2=[9,1,8,2,7,3,6,4,5]

    c1,c2 = onepoint(p1,p2)
    
    print(c1)
    print(c2)
