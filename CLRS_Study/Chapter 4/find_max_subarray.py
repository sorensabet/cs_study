import numpy as np
import scipy as sc

# My objective in writing this is to figure out how it works. 


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -10e5
    summ = 0
    max_left = 0
    
    for i in range(mid,low-1,-1):
        summ += A[i]
        if summ > left_sum:
            left_sum = summ;
            max_left = i;
        print('lsum: %d, sum: %d, A[i]: %d, max_left: %d' % (left_sum, summ, A[i], max_left))
        input('')
    
    right_sum = -10e5
    summ = 0
    max_right = 0
    
    for j in range(mid+1, high):
        summ = summ + A[j]
        if (summ > right_sum):
            right_sum = summ 
            max_right = j
        print('rsum: %d, sum: %d, A[i]: %d, max_left: %d' % (right_sum, summ, A[j], max_right))
        input('')
    
    
    return max_left, max_right, left_sum + right_sum
    
        
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

ml, mr, s = find_max_crossing_subarray(A, 0, 7, len(A)-1)