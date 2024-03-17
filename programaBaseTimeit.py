import timeit

starTime= timeit.default_timer()
n = 10000000
lst = range(n)
x = 2.0
v = list(lst)

for i in lst:
    v[i] = v[i] * x
endTime= timeit.default_timer()
print(f"Tiempo recorrido {endTime - starTime}")