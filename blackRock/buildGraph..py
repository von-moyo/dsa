import sys
from collections import defaultdict
# import numpy as np
# import pandas as pd
# from sklearn import ...

Input = list(sys.stdin)
n = len(Input)
pair = Input[0].split("/")
pair[-1] = pair[-1][:-1]

# Initialize adjacency list
adjacencyList = defaultdict(list)

# Build ajdacency list
for  i in range(1, n):
    employees = Input[i].split("/")
    employees[1] = employees[1][:-1]
    adjacencyList[employees[0]].append(employees[1])
    
visited = set()
def beadthFirstSearch(employee, target, count):
    visited.add(employee)
    if employee == target:
        return count
    for emp in adjacencyList[employee]:
        if emp not in visited:
            level = beadthFirstSearch(emp, target, count + 1)
            if level:
                return level
    return 0

print(beadthFirstSearch(pair[0], pair[1], 0))