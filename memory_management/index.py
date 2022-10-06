import sys
import tracemalloc

import test
if __name__ == "__main__":
    tracemalloc.start()
    a = test.defaultdict(int)
    print(test.Counter("prince"))
    print(tracemalloc.get_traced_memory())



