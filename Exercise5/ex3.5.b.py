"""
Class: ENSF 338, W23
Names: Hareem Khan, Eeman Abid
Assignment: 3

"""
#Task B:Insertion in and extraction from priority queue

import random
import time
import statistics
import matplotlib.pyplot as plt
import heapq


import random
import time
from heapq import heappop, heappush

# Inefficient Implementation
def inefficient_pqueue(num_elements):
    pqueue = []
    for i in range(num_elements):
        heappush(pqueue, random.randint(0, 100))
    for i in range(num_elements):
        heappop(pqueue)

# Efficient Implementation
def efficient_pqueue(num_elements):
    pqueue = []
    for i in range(num_elements):
        heappush(pqueue, random.randint(0, 100))
    while pqueue:
        heappop(pqueue)

# Experiment Code
num_measurements = 100
num_elements = 1000

inefficient_times = []
efficient_times = []

for i in range(num_measurements):
    # Inefficient Implementation
    start = time.time()
    inefficient_pqueue(num_elements)
    end = time.time()
    inefficient_times.append(end-start)

    # Efficient Implementation
    start = time.time()
    efficient_pqueue(num_elements)
    end = time.time()
    efficient_times.append(end-start)

# Plot Distribution
import matplotlib.pyplot as plt

plt.hist(inefficient_times, bins=10, alpha=0.5, label='Inefficient')
plt.hist(efficient_times, bins=10, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.xlabel("Values")
plt.ylabel("Measurements")
plt.show()

# Print Aggregate of Measured Values
print(f'Inefficient: min={min(inefficient_times)}, avg={sum(inefficient_times)/num_measurements}')
print(f'Efficient: min={min(efficient_times)}, avg={sum(efficient_times)/num_measurements}')
