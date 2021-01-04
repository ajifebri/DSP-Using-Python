import numpy as np

def impseq(n0, n1, n2):
    ''' Generates x(n) = delta(n-n0)
    n1 <= n <= n2 '''
    n = np.array([i for i in range(n1, n2+1)])
    x = np.zeros((len(n),))
    x[(n-n0)==0] = 1

    return x, n

#x, n = impseq(0, -3, 4)
#print(n)
#print(x)

def stepseq



    
