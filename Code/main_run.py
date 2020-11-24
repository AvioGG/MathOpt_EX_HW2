# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 07:31:49 2020

@author: HASAN NAZIM
"""
import numpy as np
from bubblesort import bubble_sort
from mergesort import merge_sort

if __name__ == "__main__":
        
    A=np.random.randint(-50,50,100)
    #print(A)   
    K1=bubble_sort(A)
    print(K1)
    K2=np.sort(A)
    if(np.array_equal(K1,K2)):
        print("equal-bubblesort")    
    print("======================================")
    K4=merge_sort(A)
    print(K4)
    K5=np.sort(A)
    if(np.array_equal(K4,K5)):
        print("equal-mergesort")    
        
