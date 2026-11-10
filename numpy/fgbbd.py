# #Задача 1
# import time
# import numpy as np
#
# rng = np.random.default_rng(42)
# a = rng.normal(size=1_000_000)

# def loop_sum_rows(mat):
#     total = 0.0
#     for x in mat:
#         total += x
#     return total
#
#
# def numpy_sum_rows(mat):
#     return mat.sum()
#
#
# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best
#
#
# r_loop,  t_loop  = measure(loop_sum_rows,  a)
# r_numpy, t_numpy = measure(numpy_sum_rows, a)
#
# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
#
#
#
#
# #Задача 2
# import time
# import numpy as np
#
# rng = np.random.default_rng(42)
# a = rng.normal(size=1_000_000)
#
#
# def loop_sum_rows(mat):
#     import math
#     n = len(mat)
#     s = 0.0
#     sq = 0.0
#     for x in mat:
#         s += x
#         sq += x * x
#     mean = s / n
#     std = math.sqrt(sq / n - mean * mean)
#     return mean, std
#
#
# def numpy_sum_rows(mat):
#     return mat.mean(), mat.std()
#
#
# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best
#
#
# r_loop,  t_loop  = measure(loop_sum_rows,  a)
# r_numpy, t_numpy = measure(numpy_sum_rows, a)
#
# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


#Задача 3
# import time
# import numpy as np
# import math
#
# rng = np.random.default_rng(42)
# a = rng.normal(size=1_000_000)
#
# def loop_sum(arr):
#  return [math.sin(x) + x * x for x in arr]
#
# def numpy_sum(arr):
#  return np.sin(arr) + arr ** 2
#
# def measure(fn, data, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(data)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best
#
# r_loop, t_loop = measure(loop_sum, a)
# r_numpy, t_numpy = measure(numpy_sum, a)
#
# print(f"Цикл:  {t_loop*1000:8.2f} мс")
# print(f"NumPy: {t_numpy*1000:8.2f} мс")
# print(f"Ускорение: {t_loop/t_numpy:.1f}×")
# print(f"Совпадают: {np.allclose(r_loop, r_numpy)}")

