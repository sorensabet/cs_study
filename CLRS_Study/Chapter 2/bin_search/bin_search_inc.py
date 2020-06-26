# Incremental binary search in Python
# Soren Sabet Sarvestany 
# CLRS 


# I know there are cleaner ways of writing this because I"ve seen it before but I couldn't figure it out today for some reason. 
import math
import numpy as np

def rec_bin_search(a,b,v):
    if a > b:
        return np.nan
    m = np.floor((a+b)/2)
    if m == v:
        return m 
    if m < v:
        return rec_bin_search(a,m,v)
    return rec_bin_search(m+1,b,v)

#def bin_search(A,v):
#    if (len(A) == 0):
#        return np.nan
#    
#    low=0;
#    high=len(A)-1
#    if (v < A[low] or v > A[high]):
#        return np.nan
#    
#    mid = math.floor((high+low)/2)
#    
#    it_count = 0;
#    while (low <= high):
#        if (A[mid] > v):
#            high = mid
#        elif (A[mid] < v):
#            low = mid
#        mid = math.floor((high+low)/2)
#        
#        if (A[mid] == v):
#            return mid
#        elif (A[low] == v):
#            return low
#        elif (A[high] == v):
#            return high
#        elif (low+1==high):
#            return np.nan
#        
#        print('Low: ' + str(low))
#        print('Hig: ' + str(high))
#        print('Mid: ' + str(mid))
#        print('it: ' + str(it_count))
#        input('')
#        it_count += 1
        

A = [0,1,2]
v = 0

#ans = bin_search(A,v)
ans = rec_bin_search(0, len(A), v)

print('Answer: ' + str(ans))
