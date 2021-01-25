
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 1000)

Vc = 5
fc = 1000  # 1Khz
Mc = 100   # 100-sample periodicity
Ts = 1/(Mc*fc)
vc = Vc * np.sin(2*np.pi*n/Mc)

Vm = 2
fm = 100
Mm = 500 
vm = Vm * np.sin(2*np.pi*n/Mm)

v1 = Vc + vm
v2 = v1 * np.sin(2*np.pi*n/Mc)

plt.grid()
plt.plot(n, vc, 'green')
plt.plot(n, v2, 'blue')
plt.plot(n, v1, 'red')
plt.show()
