from typing import List
def getBiggestShared(a: List[int], b: List[int]) -> int:
    Shared = 0 
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if Shared < a[i]:
                    Shared = a[i]
    
    return Shared



a = [1, 2, 4, 5]
b = [3, 4, 7, 11]

print (getBiggestShared (a, b))