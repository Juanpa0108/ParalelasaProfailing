import cProfile as profile
import pstats

prof = profile.Profile()


n = 10000000
lst = range(n)
x = 2.0
v = list(lst)

prof.enable()
for i in lst:
    v[i] = v[i] * x

prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(5)