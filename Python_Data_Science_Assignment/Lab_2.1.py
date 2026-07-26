import numpy as np
import time 

#Generating 1 million random integers
integers = np.random.randint(1,101,1000000)

#Python loop 
start = time.time()
squared_loop = []
for number in integers:
    squared_loop.append(number**2)
    loop_time=time.time() - start

#Numpy Vectorization
start = time.time()
squared_loop=integers**2
npy_time=time.time() - start

print("Python loop time:", loop_time) 
print("NumPy time:", npy_time)

