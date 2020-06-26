# Comparing function sizes 

import numpy as np
import matplotlib.pyplot as plt
import math

def iter_log(n):
    if (n <= 1):
        return 0;
    else:
        return 1 + iter_log(np.log(n))

numb = 1500
n = np.linspace(1,numb,num=numb)

mat = np.ndarray([len(n),31])
mat[:,0] = n
mat[:,3] = n**(0.5)
mat[:,4] = n**2
mat[:,7] = 1.5**n
mat[:,8] = n**3
mat[:,9] = np.log2(n)*np.log2(n)
mat[:,11] = 2**2**n
mat[:,12] = n**(1/np.log2(n))
mat[:,13] = 1;
mat[:,14] = np.log2(n)

# Col 1: n
# Col 2: lg(lg*n)
# Col 3: 2^lg*n

for elem in n: 
    mat[int(elem)-1,1] = iter_log(elem)
    mat[int(elem)-1,2] = 2**iter_log(elem)
    #mat[int(elem)-1,5] = np.math.factorial(elem)
    #mat[int(elem)-1,6] = np.math.factorial(math.ceil(np.log2(elem)))

mat[:,10] = np.log2(mat[:,5])

#plt.plot(mat[:,0], mat[:,1], label='lg(lg*n)')
plt.plot(mat[:,0], mat[:,2], label='2^(lg*n)')
plt.plot(mat[:,0], mat[:,3], label='n^0.5')
#plt.plot(mat[:,0], mat[:,4], label='n^2')
#plt.plot(mat[:,0], mat[:,5], label='n!')
#plt.plot(mat[:,0], mat[:,6], label='(lgn)!')z
#plt.plot(mat[:,0], mat[:,7], label='1.5^n')
#plt.plot(mat[:,0], mat[:,8], label='n^3')
#plt.plot(mat[:,0], mat[:,9], label='lg^2 n')
#plt.plot(mat[:,0], mat[:,10], label='lg(n!)')
#plt.plot(mat[:,0], mat[:,11], label='2^2^n')
#plt.plot(mat[:,0], mat[:,12], label='n^(1/lg(n))')
plt.plot(mat[:,0], mat[:,14], label='ln(n)')



plt.legend(loc=1)