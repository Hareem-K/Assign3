"""
Class: ENSF 338, W23
Names: Hareem Khan, Eeman Abid
Assignment: 3

"""

#Task a: Search in a sorted Array



import time
import random
import matplotlib.pyplot as plt

#inneficient Implementation
def search_sorted_array(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Efficient Implementation
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def time_search_sorted_array(func, n):
    arr = sorted(random.sample(range(1, n*10), n))
    target = random.randint(1, n*10)
    times = []
    for i in range(100):
        start_time = time.time()
        func(arr, target)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

n = 1000
inefficient_times = time_search_sorted_array(search_sorted_array, n)
efficient_times = time_search_sorted_array(binary_search, n)

plt.hist(inefficient_times, alpha=0.5, label='Inefficient')
plt.hist(efficient_times, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.xlabel("Values")
plt.ylabel("Measurements")
plt.show()

print("Inefficient average execution time: ", sum(inefficient_times) / len(inefficient_times))
print("Efficient average execution time: ", sum(efficient_times) / len(efficient_times))
