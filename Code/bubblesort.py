import numpy as np

def bubble_sort(A):    
    not_sorted=True
    while(not_sorted):
        not_sorted=False
        for i in range(len(A)-1):
            if(A[i+1]<A[i]):
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
                not_sorted=True
    return A
