# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:33:10 2017

@author: JoJo
"""
class ant:
    def __init__(self, path, totalcost):
        self.path = []
        self.totalcost = 0

def read_file(filename):
    tspmat = open(filename,".tsp")
    return tspmat

