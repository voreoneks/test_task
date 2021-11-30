import sys
import math

data_file = sys.argv[1]
total = 0
steps = 0

with open(data_file, 'r') as file:
    arr = [int(x) for x in file]

for item in arr:
    total += item

average = math.ceil(total / len(arr))

for item in arr:
    if item > average:
        while(item != average):
            steps += 1
            item -= 1
    elif item < average:
        while(item != average):
            steps += 1
            item += 1
    else:
        continue
 
print(steps)