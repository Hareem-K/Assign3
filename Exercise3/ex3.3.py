import sys

list =[]
old_capacity= sys.getsizeof(list)

for x in range(64):
    list.append(x)
    if sys.getsizeof(list) != old_capacity:
        new_capacity = sys.getsizeof(list)
        print(f"Capacity changed from {old_capacity} to {new_capacity} bytes after adding {x+1} elements.")