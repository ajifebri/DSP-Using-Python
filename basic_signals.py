import numpy as np

def impseq(n0, n1, n2):
    ''' Generates x(n) = delta(n-n0)
    n1 <= n <= n2 '''
    n = np.array(range(n1, n2+1))
    x = np.zeros((len(n),))
    x[(n-n0)==0] = 1

    return x, n

#x, n = impseq(0, -3, 4)
#print(n)
#print(x)

def stepseq(n0, n1, n2):
    ''' Generates x(n) = u(n-n0) 
    n1 <= n <= n2'''
    n = np.array(range(n1, n2+1))
    x = np.zeros((len(n),))
    x[(n-n0)>=0] = 1

    return x, n

#x, n = stepseq(0, -3, 4)
#print(n)
#print(x)

# Exponential sequence
n1 = 0
n2 = 10
n = np.array(range(n1, n2+1))
x = np.power(0.9, n)
print(n)
print(x)




    
