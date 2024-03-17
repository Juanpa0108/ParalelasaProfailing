import numpy as np
import cProfile as profile
import pstats

prof = profile.Profile()



n = 10000000
lst = range(0,n)
x = 2
v = np.array(lst)

prof.enable()
for i in lst:
  v[i] = v[i] * x

prof.disable()

stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(5)