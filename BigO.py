# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:50:45 2019

@author: John
"""
#TO DO - I WANT TO GRAPH O(N) FOR BOTH ALGOS ON SAME GRAPH THEN FIN
#http://interactivepython.org/runestone/static/pythonds/Introduction/ExceptionHandling.html
import time
from random import randrange

#Do an O(N^2) algorithm to find min number in a list
#Then do an O(N) version 

def findMin1(alist):
    for i in alist:
        smallest = True
        for j in alist:
            if j < i:
                smallest = False
        if smallest == True:
            smallestNum = i
    return smallestNum
 
def findMin2(alist):
    smallestNum = 1000 
    for i in alist:
        if i < smallestNum:
            smallestNum = i
    return smallestNum

for listsize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listsize)]
    start = time.time()
    print (str(findMin2(alist)))
    end = time.time()
    print ("size: %d time %f" % (listsize, end-start))
    
