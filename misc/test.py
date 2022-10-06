
from functools import wraps
import time
import pdb



def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def cal():
    a = []
    for i in range(1000):
        a.append(i)






if __name__ == "__main__":
    pdb.set_trace()
    cal()