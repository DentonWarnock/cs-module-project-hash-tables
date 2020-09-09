# Your code here
import math
import random
import time

cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    #
    # if (x, y) is a new input, run slow fn and cache results
    # otherwise return cached results
    #
    ### very interesting to note that the program runs slowly at first while caching all the (x, y) possibilites then very fast after
    
    if (x, y) not in cache:
        cache[(x, y)] = slowfun_too_slow(x, y)
    return cache[(x,y)]


# Do not modify below this line!

start = time.time()
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
print(f'\nRuntime: {time.time()-start:.2f} seconds')

