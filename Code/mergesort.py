import numpy as np

def merge_sort(A):
    if(len(A)!=1):
        mid=len(A)//2#first index of second(right) half
        L=merge_sort(A[0:mid])#use method recursively for left array
        R=merge_sort(A[mid:]) #use method recursively for right array
        A=merger(L,R) #combine left and right arrays and set it to A
    return A

def merger(L,R):
    merged=np.zeros(len(L)+len(R))
    index_L=0
    index_R=0        
    while((index_L+index_R)<(len(R)+len(L))):
        if(index_L==len(L)):
            # check if left part is fully traversed
            # if so, continue from the right side
            merged[index_L+index_R]=R[index_R]
            index_R += 1          
        elif(index_R==len(R)):
            # check if right part is fully traversed
            # if so, continue from the left side
            merged[index_L+index_R]=L[index_L]
            index_L += 1
        elif(L[index_L]<R[index_R]):
            #compare left and right arrays with respective indexes
            merged[index_L+index_R]=L[index_L]
            index_L += 1
        elif(L[index_L] >= R[index_R]):
            #compare left and right arrays with respective indexes
            merged[index_L+index_R]=R[index_R]
            index_R += 1        
    return merged
