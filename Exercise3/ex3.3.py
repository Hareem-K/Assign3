"""
Class: ENSF 338, W23
Names: Hareem Khan, Eeman Abid
Assignment: 3
"""

import sys

list =[]
old_capacity= sys.getsizeof(list)

for x in range(64):
    list.append(x)
    if sys.getsizeof(list) != old_capacity:
        new_capacity = sys.getsizeof(list)
        print(f"The total capacity changed from {old_capacity} to {new_capacity} bytes after adding {x+1} elements. The new number of elements that can be stored is {new_capacity/8}")
        old_capacity = new_capacity