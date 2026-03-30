import timeit

code = """
for i in range(1000000):
    pass
"""

execution_time = timeit.timeit(code, number=1)
print(execution_time)