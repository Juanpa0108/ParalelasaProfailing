import numpy as np
import timeit

starTime= timeit.default_timer()

n = 10000000
lst = range(0,n)
x = 2
v = np.array(lst)

for i in lst:
  v[i] = v[i] * x

endTime= timeit.default_timer()
print(f"Tiempo recorrido {endTime - starTime}")