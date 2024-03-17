import ctypes
import cProfile as profile
import pstats

prof = profile.Profile()
# Tamaño del vector y el escalar
vectorSize = 10000000
scalar = 2.0

# Crear el vector y el resultado como listas de Python
prof.enable()
vector = [float(i + 1) for i in range(vectorSize)]
result = [0.0] * vectorSize

# Cargar la biblioteca dinámica
libMultScalar = ctypes.CDLL('./libMultScalar.so')

# Definir el tipo de datos de la función
libMultScalar.vectorScalarMultiply.restype = None
libMultScalar.vectorScalarMultiply.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# Convertir el vector y el resultado a punteros de ctypes
vector_ptr = (ctypes.c_double * len(vector))(*vector)
result_ptr = (ctypes.c_double * len(result))(*result)

# Llamar a la función C
libMultScalar.vectorScalarMultiply(vector_ptr, scalar, result_ptr, vectorSize)
prof.disable()

stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(5)