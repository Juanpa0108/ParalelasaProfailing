import ctypes
import timeit

starTime = timeit.default_timer()
vectorSize = 10000000
scalar = 2.0

vector = [float(i + 1) for i in range(vectorSize)]
result = [0.0] * vectorSize

libMultScalar = ctypes.CDLL('./libMultScalar.so')
libMultScalar.vectorScalarMultiply.restype = None
libMultScalar.vectorScalarMultiply.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int]


vector_ptr = (ctypes.c_double * len(vector))(*vector)
result_ptr = (ctypes.c_double * len(result))(*result)

libMultScalar.vectorScalarMultiply(vector_ptr, scalar, result_ptr, vectorSize)
endTime = timeit.default_timer()

print(f"Tiempo transcurrido {endTime - starTime}")