# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:33:10 2017

@author: JoJo
"""

import numpy as np

class ant:
    def __init__(self, path, totalcost):
        self.path = []
        self.totalcost = 0

def read_file(filename):
    """This function reads in the tsp files and converts them into int matrices. The matrix can be accessed globably with the variable name tspmat
    """
    if filename == 1:
        tspmat = np.loadtxt("1.tsp")
    
    if filename == 2:
        tspmat = np.loadtxt("2.tsp")
        
    if filename == 3:
        tspmat = np.loadtxt("3.tsp")
        
    valuematrix = tspmat.astype(int)
    return valuematrix

def initalize(benchmark, antnmbr):
    global tspmat
    tspmat = read_file(benchmark)
    
def user_input():
    benchmark = int(input("Please specify TSP benchmark to use [1],[2],[3]: "))
    antnmbr = int(input("Please specify number of ants to be used: "))
    
    initalize(benchmark, antnmbr)
    
    
user_input()