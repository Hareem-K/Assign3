"""
Class: ENSF 338, W23
Names: Hareem Khan, Eeman Abid
Assignment: 3
"""

import json
import requests
import time
import matplotlib.pyplot as plt

# Create array and tasks json files
array_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json'
array_request = requests.get(array_url)
open('ex2data.json', 'wb').write(array_request.content)

tasks_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json'
tasks_request = requests.get(tasks_url)
open('ex2tasks.json', 'wb').write(tasks_request.content)

# Load the array
with open('ex2data.json', 'r') as arr:
    array = json.load(arr)

# Load the list of search tasks
with open('ex2tasks.json', 'r') as task:
    tasks = json.load(task)
    
    
def binary_search(array, target, start, end, midpoint):
    if start > end:
        return False
    
    mid = midpoint
    
    if mid < start or mid > end:
        mid = (start + end) // 2
    
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end, (start + end) // 2 + 1)
    else:
        return binary_search(array, target, start, mid - 1, (start + end) // 2 - 1)


# Define a function to find the best midpoint for each task
def find_best_midpoint(arr, tasks):
    midpoints = []
    for task in tasks:
        # Define the range of midpoints to try based on the length of the array
        start = 0
        end = len(arr) - 1
        midpoints_to_try = [int(0.10 * len(array)), int(0.20 * len(array)),  int(0.30 * len(array)), int(0.40 * len(array)), int(0.50 * len(array)), int(0.60 * len(array)), int(0.70 * len(array)), int(0.80 * len(array)), int(0.9 * len(array))]
        
        # Time each midpoint and choose the fastest one
        best_midpoint = (start + end) // 2
        best_time = float('inf')
        for midpoint in midpoints_to_try:
            start_time = time.time()
            binary_search(arr, task, start, end, midpoint)
            end_time = time.time()
            search_time = end_time - start_time
            if search_time < best_time:
                best_time = search_time
                best_midpoint = midpoint
        midpoints.append(best_midpoint)
    return midpoints


if __name__ == '__main__':
    # Find the best midpoint for each task
    midpoints = find_best_midpoint(array, tasks)

    # Plot the results
    plt.scatter(tasks, midpoints, color='pink')
    plt.xlabel('Task to Search')
    plt.ylabel('Best Midpoint')
    plt.title('Performance of Binary Search With Different Midpoints')
    plt.show()